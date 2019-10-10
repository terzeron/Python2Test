#!/usr/bin/env python

import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://www.amazon.com/Art-Computer-Programming-Fundamental-Algorithms/dp/0201896834/ref=pd_bbs_sr_2?ie=UTF8&s=books&qid=1207844307&sr=8-2")
soup = BeautifulSoup(page)
for incident in soup('td', width="90%"):
    where, linebreak, what = incident.contents[:3]
    print where.strip()
    print what.strip()
    print 
