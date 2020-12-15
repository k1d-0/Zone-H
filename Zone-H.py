#!/usr/bin/python
# vim: set fileencoding=\xe2
import re
from urlparse import urlparse
from pprint import pprint

print '''
######################################
#  ____                 _  _         #
# |_  /___ _ _  ___ ___| || |        #
#  / // _ \ ' \/ -_)___| __ |        #
# /___\___/_||_\___|   |_||_|        #
######################################                                               
      '''


urls = raw_input('Text File To Get ? : ')
with open(urls, 'r') as urls:
	for line in urls:
		url = line.rstrip() and line.split('\t')

		bond = url[7].replace('...', '')
		benz = url[7].split('/')
		get = benz[0]
		if 'http://' not in get:
			url = 'http://'+get
			with open('hd.txt', 'a') as myfile:
			 myfile.write('http://'+get)
			 myfile.write('\n')
