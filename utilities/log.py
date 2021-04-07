import logging
import sys


# Log template
class LogTemplate:
    SIMPLE = "%(color_on)s%(levelname)8s | %(filename)s: %(funcName)s (line %(lineno)d) -- %(message)s%(color_off)s"
    SERVER = "%(color_on)s[%(asctime)s] [%(levelname)-8s] [%(threadName)s] [%(filename)s]  %(message)s%(color_off)s"
    FULL = "%(color_on)s[%(asctime)s] [%(levelname)-8s] [%(threadName)s] [%(filename)s] [%(funcName)s] [line %(lineno)d] %(message)s%(color_off)s"


# Logging formatter supporting colored output
class LogFormatter(logging.Formatter):

    COLOR_CODES = {
        logging.CRITICAL: "\033[1;31m",  # red
        logging.ERROR: "\033[0;31m",  # bright red
        logging.WARNING: "\033[0;33m",  # bright/bold yellow
        logging.INFO: "\033[0;36m",  # white / light gray
        logging.DEBUG: "\033[0m",  # bright/bold black / dark gray
    }

    RESET_CODE = "\033[0m"

    def __init__(self, color, *args, **kwargs):
        super(LogFormatter, self).__init__(*args, **kwargs)
        self.color = color

    def format(self, record, *args, **kwargs):
        if self.color and record.levelno in self.COLOR_CODES:
            record.color_on = self.COLOR_CODES[record.levelno]
            record.color_off = self.RESET_CODE
        else:
            record.color_on = ""
            record.color_off = ""
        return super(LogFormatter, self).format(record, *args, **kwargs)


def setup_logger(
    logger_name=None, output="stdout", level="DEBUG", template="simple", color=True
) -> None:

    # Get logger, if no logger name given gets root.
    logger = logging.getLogger(logger_name)

    # Set global log level to 'debug' (required for handler levels to work)
    logger.setLevel(logging.DEBUG)

    # Create console handler
    output = output.lower()
    if output == "stdout":
        output = sys.stdout
    elif output == "stderr":
        output = sys.stderr
    else:
        print("Failed to set console output: invalid output: '%s'" % output)
        return False
    console_handler = logging.StreamHandler(output)

    # Set console log level
    try:
        console_handler.setLevel(level.upper())  # only accepts uppercase level names
    except:
        print("Failed to set console log level: invalid level: '%s'" % level)
        return False

    # Create and set formatter, add console handler to logger
    template = template.lower()
    if template == "full":
        format_ = LogTemplate.FULL
    elif template == "server":
        format_ = LogTemplate.SERVER
    elif template in ["simple", "dev"]:
        format_ = LogTemplate.SIMPLE
    else:
        print(f"LOG INVALID MODE '{template}'. Valid modes: full, server, simple")
        return False
    console_formatter = LogFormatter(fmt=format_, color=color)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)


# alias
get_logger = logging.getLogger

if __name__ == "__main__":

    setup_logging(level="debug", template="dev")
    logger = get_logger()
    print(logger, id(logger))

    try:
        a = 4 / 0
    except Exception as exc:
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.error("shit", exc_info=exc)
        logger.critical("holy shit")
