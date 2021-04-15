#!/usr/bin/python3

# updated for Python 3

import urllib.request
import sys

# sys.argv[1] = url
# sys.argv[2] = file name


response = urllib.request.urlretrieve(sys.argv[1], sys.argv[2])
