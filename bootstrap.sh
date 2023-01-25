#!/bin/sh

export FLASK_APP=./src/module1/index.py

pipenv run flask --debug run -h 0.0.0.0