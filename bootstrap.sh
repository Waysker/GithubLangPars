#!/bin/sh
export FLASK_APP=./LangPars/index.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0