import os
from dataclasses import dataclass

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


@dataclass(frozen=True)
class Config:
    PROJECT_NAME: str = os.environ.get("PROJECT_NAME", default="OCR PLAYGROUND")
    LOCAL_DEVELOPMENT: bool = os.environ.get("LOCAL_DEVELOPMENT", default=True)
    AWS_ACCESS_KEY_ID: str = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_REGION_NAME: str = os.environ.get("AWS_REGION_NAME")


config = Config()
