from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
import re
import datetime
import sys
import csv
import time

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
	enc = file.encoding
	if enc == 'UTF-8':
		print(*objects, sep=sep, end=end, file=file)
	else:
		f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
		print(*map(f, objects), sep=sep, end=end, file=file)

def ParseFOMC(dateString):
	url='http://www.federalreserve.gov/newsevents/press/monetary/' + dateString + 'a.htm'
	try:
		print('Parsing:'+url)
		html=urlopen(url)
		webpage=BeautifulSoup(html.read(),'html.parser')
		#results=webpage.find(attrs={'class':'prTime'})
		#results = results.nextSibling.nextSibling.text.replace('\n', ' ').strip()
		#results = re.sub(' +', ' ', results)
		#results = results.replace('  ', ' ')
		results=webpage.find_all('p',attrs={'class':None})
		output=''
		for result in results:
			output=output+result.text+' '
		return output
	except HTTPError as e:
		print(e)

inputFile=open('FOMCDates.csv','r')
for line in inputFile:
	sLine=line.replace('\n','')
	if sLine!='Statement':
		sDate='20'+sLine[6:8]+sLine[0:2]+sLine[3:5]
		outputFile=open('FOMC/FOMCStatement-'+sDate+'.txt','w',encoding='utf-8')
		outputFile.write(ParseFOMC(sDate))
		outputFile.close
		time.sleep(1)