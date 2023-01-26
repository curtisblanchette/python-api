#!/bin/sh

export FLASK_APP=./module1/index.py

pipenv run flask --debug run -h 0.0.0.0