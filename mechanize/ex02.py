#!/usr/bin/env python

import mechanize
response = mechanize.urlopen("http://code.google.com")
print response.read()
