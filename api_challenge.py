import urllib
import json
import httplib
import urllib2
import requests


url = 'http://challenge.code2040.org/api/register'
reqDict = {'email':'e.faroni@berkeley.edu', 'github': 'https://github.com/efaroni/APIChallenge.git'}
req = requests.post(url, data = None, json = reqDict)

print(req.text)
#{"result":"wiBwn5OEbL"}
