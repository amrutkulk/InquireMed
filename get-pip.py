#!/usr/bin/env python
# WARNING: this file is meant to be run with python3.6+ and not intended for production use.
import sys
from urllib.request import urlopen

exec(urlopen("https://bootstrap.pypa.io/get-pip.py").read())
