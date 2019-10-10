#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup

html = "<html><p>Para 1<p>Para 2<blockquote>Quote 1<blockquote>Quote 2"
soup = BeautifulSoup(html)
print soup.prettify()
