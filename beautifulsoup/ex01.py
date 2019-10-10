#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import re

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']
soup = BeautifulSoup(''.join(doc))

print soup.prettify()

print soup.contents[0].name
print soup.contents[0].contents[0].name

head = soup.contents[0].contents[0]
print head.parent.name
print head.next
print head.nextSibling.name
print head.nextSibling.contents[0]
print head.nextSibling.contents[0].nextSibling

titleTag = soup.html.head.title
print titleTag
print titleTag.string

print len(soup('p'))

print soup.findAll('p', align="center")
print soup.findAll('p', align="center")[0]
print soup.find('p', align="center")
print soup('p', align="center")[0]['id']
print soup.find('p', align=re.compile('^b.*'))['id']
print soup.find('p').b.string
print soup('p')[1].b.string

titleTag['id'] = 'theTitle'
titleTag.contents[0].replaceWith("New title")
print soup.html.head

soup.p.extract()
print soup.prettify()
print soup.p.replaceWith(soup.b) # error

soup.body.insert(0, "This page used to have ")
soup.body.insert(2, " &lt;p&gt; tags!")
print soup.body

