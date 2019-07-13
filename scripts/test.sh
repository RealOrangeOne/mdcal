#!/usr/bin/env bash

set -e

export PATH=env/bin:${PATH}

if hash black 2>/dev/null;
then
    echo "> Running formatter..."
    black --check setup.py mdcal
fi

echo "> Running linter..."
flake8 --ignore=E128,E501,W503 setup.py mdcal

echo "> Running isort..."
isort -rc -c setup.py mdcal


echo "> Running type checker..."
mypy mdcal
