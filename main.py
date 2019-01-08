#!/usr/bin/env python

import requests

print(requests.__version__)

r = requests.get('http://google.com')

print(r.status_code)
print(r.headers)
print(r.encoding)
