#!/usr/bin/env python

import re
from mechanize import Browser

br = Browser()
#br.select_form(name="order")
br.open("http://terzeron.net");
#for form in br.forms():
br.select_form(nr=0)
br["musician"] = "Michael Jackson"
response2 = br.submit()
print response2.info()
print response2.read()
