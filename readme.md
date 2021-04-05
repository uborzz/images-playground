# playground env
personal multipurpose python environment for image treating in ubuntu 20.04 and python 3.8.5 with vscode

## binaries
In case no binary deps already installed. This installs qt, tesseract, poppler and ghostscript in the system

```bash
chmod +x install-bins.sh
./install-bins.sh
```

## virtual env
In this case pip works better, so im just using pipenv for the env generation

```bash
pipenv shell
pip install -r reqs.txt
```

## links to qt
directly use our local qt installation

```bash
ln -s /usr/lib/python3/dist-packages/PyQt5/ <path_to_venv>/lib/python3.8/site-packages/ 
ln -s /usr/lib/python3/dist-packages/sip.cpython-38-x86_64-linux-gnu.so <path_to_venv>/lib/python3.8/site-packages/
```

## more libs and dev tools
```bash
pip install -r reqs-extra.txt
pip install -r reqs-dev.txt
```

## vscode interpreter
.vscode/settings.json
```json
{
    ...
    "python.pythonPath": "<path_to_env>/bin/python"
    ...
}
```

## check installation
with the virtualenv activated!!

### imports and libs
```bash
python check-installs/run.py
```

### jupyter
```bash
jupyter notebook
```