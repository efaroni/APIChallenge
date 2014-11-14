import urllib
import json
import httplib
import urllib2
import requests


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
