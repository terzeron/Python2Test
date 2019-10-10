#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup

html = """
<html>
<form>
 <table>
 <td><input name="input1">Row 1 cell 1
 <tr><td>Row 2 cell 1
 </form> 
 <td>Row 2 cell 2<br>This</br> sure is a long cell
</body> 
</html>"""

print BeautifulSoup(html).prettify()
