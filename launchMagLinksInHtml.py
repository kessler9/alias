#!/bin/python
from bs4 import BeautifulSoup as BS
from pprint import pprint
from glob import glob
import os
import re

for html in [open(x).read() for x in glob('*.html')]:
	for mag_link in [link for link in [a['href'] for a in BS(html).find_all('a')] if link[:6] == 'magnet']:
		command = "transmission-remote -a '%s'" % mag_link
		pprint(command)
		os.popen(command).read()
