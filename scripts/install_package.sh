#!/usr/bin/env bash

rm -rf dist

python setup.py sdist

pip install dist/*  --upgrade