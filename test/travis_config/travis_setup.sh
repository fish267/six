#!/usr/bin/env bash

# Just to be sure
pip install -U pip
# pip is not able to install distribute: "ImportError: No module named _markerlib"
easy_install distribute

pip install -U coverage
pip install coveralls

# Server back-ends and template engines. Not all back-ends support all python versions and we only want to test for 2.7 and 3.6 to keep things sane
pip install mako jinja2 waitress "cherrypy<9" cheroot paste tornado twisted diesel meinheld gunicorn eventlet
pip install uvloop
