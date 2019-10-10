#!/usr/bin/env python

import re
from mechanize import Browser

br = Browser()
br.open("http://code.google.com/")

# follow second link with element text matching regular expression
#reponse1 = br.follow_link(text_regex=r"opensource", nr=1)
response1 = br.follow_link(url="/opensource/")
assert br.viewing_html()
print br.title()
print response1.geturl()
print response1.info() # headers
print response1.read() # body
response1.close() # shown for clarity; in fact Browser does this for you

