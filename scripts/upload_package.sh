#!/usr/bin/env bash

rm -rf dist
python setup.py bdist_wheel

twine upload -u fish267 -p H9VacVl6b46y  dist/*
