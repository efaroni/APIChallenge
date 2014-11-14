import urllib
import json
import httplib
import urllib2
import requests
import dateutil.parser
import datetime

#Retrieving my token from API
url = 'http://challenge.code2040.org/api/register'
reqDict = {'email' : 'e.faroni@berkeley.edu', 'github' : 'https://github.com/efaroni/APIChallenge.git'}
req = requests.post(url, data = None, json = reqDict)
req_json = req.json()
for key in req_json.keys():
	token = req_json[key]


#Beginning stage 1
stage1_url = 'http://challenge.code2040.org/api/getstring'
stage1_dict = {'token' : token}
req2 = requests.post(stage1_url, data = None, json = stage1_dict)
req2_json = req2.json()
for key in req2_json.keys():
	str_to_reverse = req2_json[key]
reversed_str = str_to_reverse[::-1]

#Sending reversed string back
stage1_result_url = 'http://challenge.code2040.org/api/validatestring'
stage1_result_dict = {'token' : token, 'string': reversed_str}
req3 = requests.post(stage1_result_url, data = None, json = stage1_result_dict)
print(req3.text) #checks to make sure I passed stage 1

#Beginning stage 2
stage2_url = 'http://challenge.code2040.org/api/haystack'
stage2_dict = {'token' : token}
req3 = requests.post(stage2_url, data = None, json = stage2_dict)
req3_json = req3.json()
#the actual JSON dictionary is the value of the first key
req3_dict = req3_json.values()[0]
#now I have the JASON dictionary, hastack is first key, needle is second
haystack = req3_dict.values()[0]
needle = req3_dict.values()[1]
index_sol = haystack.index(needle)

#Posting stage 2 results
stage2_url_result = 'http://challenge.code2040.org/api/validateneedle'
stage2_result_dict = {'token' : token, 'needle' : index_sol}
req4 = requests.post(stage2_url_result, data = None, json = stage2_result_dict)
print(req4.text)#check stage 2 result

#Beginning stage 3
stage3_url = 'http://challenge.code2040.org/api/prefix'
stage3_dict = {'token' : token}
req6 = requests.post(stage3_url, data = None, json = stage3_dict)
req6_json = req6.json()
#the actual JSON dictionary is the value of the first key
req6_dict = req6_json.values()[0]
#according to my terminal output array is the first key, prefix is the second
array = req6_dict.values()[0]
prefix = req6_dict.values()[1]
#now to iterate through the strings in array and check if they start with prefix. If so, remove string
for str in array:
	if str.startswith(prefix):
		array.remove(str)

#Posting stage 3 results
stage3_result_url = 'http://challenge.code2040.org/api/validateprefix'
stage3_result_dict = {'token' : token, 'array' : array}
req7 = requests.post(stage3_result_url, data = None, json = stage3_result_dict)
print(req7.text)

#Beginning stage 4
stage4_url = 'http://challenge.code2040.org/api/time'
stage4_dict = {'token' : token}
req8 = requests.post(stage4_url, data = None, json = stage4_dict)
req8_json = req8.json()
#the actual JSON dictionary is the value of the first key
req8_dict = req8_json.values()[0]
#according to my terminal, datestamp is the first key and interval is the second
datestamp = req8_dict.values()[0]
interval = req8_dict.values()[1]
#convert ISO 8601 time to datetime object to use timedelta
date = dateutil.parser.parse(datestamp)
new_date = date + datetime.timedelta(seconds = interval)
#convert datetime object back to ISO 8601
new_date = new_date.isoformat()

#Posting stage 4 results
stage4_result_url = 'http://challenge.code2040.org/api/validatetime'
stage4_result_dict = {'token' : token, 'datestamp' : new_date}
req9 = requests.post(stage4_result_url, data = None, json = stage4_result_dict)
print(req9.text)
