#!/usr/bin/env bash

python setup.py bdist_wheel

twine upload   -u fish267 -p H9VacVl6b46y  dist/*