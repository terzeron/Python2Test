#!/usr/bin/env python

import re

pat = re.compile(r'^(\'([^\']*(\'\')*)*\')$')
result = pat.match("'a'")
print result.groups()[0]
result = pat.match("''")
print result.groups()[0]
result = pat.match("''''")
print result.groups()[0]
result = pat.match("'''")
if result: print result.groups()[0]
result = pat.match("'a''b'")
print result.groups()[0]
result = pat.match("'a''b'''")
print result.groups()[0]
result = pat.match("'''a''b'")
print result.groups()[0]
result = pat.match("'a''b''c'")
print result.groups()[0]
result = pat.match("'a''b''c'''")
print result.groups()[0]
result = pat.match("'''a''b''c'''")
print result.groups()[0]
