import json
import requests
import dateutil.parser
import datetime

#Retrieving my token from API
enroll_Dict = {'email' : 'e.faroni@berkeley.edu', 'github' : 'https://github.com/efaroni/APIChallenge.git'}
req = requests.post('http://challenge.code2040.org/api/register', data = None, json = enroll_Dict)
#must convert Request object to JSON
req_json = req.json()
token = req_json.values()[0]
#JSON dictionary to send for most requests
my_dict = {'token' : token}

#Beginning stage 1
req2 = requests.post('http://challenge.code2040.org/api/getstring', data = None, json = my_dict)
req2_json = req2.json()
str_to_reverse = req2_json.values()[0]
#most efficient way I know of to reverse string in python
reversed_str = str_to_reverse[::-1]

#Posting stage 1 results
stage1_result_dict = {'token' : token, 'string': reversed_str}
req3 = requests.post('http://challenge.code2040.org/api/validatestring', data = None, json = stage1_result_dict)
#check if stage 1 passed
print(req3.text)

#Beginning stage 2
req4 = requests.post('http://challenge.code2040.org/api/haystack', data = None, json = my_dict)
req4_json = req4.json()
#the actual JSON dictionary is the value of the first key
req4_dict = req4_json.values()[0]
#now I have the JSON dictionary, haystack is first key, needle is second
haystack = req4_dict.values()[0]
needle = req4_dict.values()[1]
index_sol = haystack.index(needle)

#Posting stage 2 results
stage2_result_dict = {'token' : token, 'needle' : index_sol}
req5 = requests.post('http://challenge.code2040.org/api/validateneedle', data = None, json = stage2_result_dict)
#check if stage 2 passed
print(req5.text)

#Beginning stage 3
req6 = requests.post('http://challenge.code2040.org/api/prefix', data = None, json = my_dict)
req6_json = req6.json()
#the actual JSON dictionary is the value of the first key
req6_dict = req6_json.values()[0]
#according to my terminal output array is the first key, prefix is the second
array = req6_dict.values()[0]
prefix = req6_dict.values()[1]
#iterate through the strings in array and check if they start with prefix. If so, remove string
print(array)
print(prefix)
for str in array:
	if str.startswith(prefix):
		array.remove(str)
print(array)

#Posting stage 3 results
stage3_result_dict = {'token' : token, 'array' : array}
req7 = requests.post('http://challenge.code2040.org/api/validateprefix', data = None, json = stage3_result_dict)
#check if stage 3 passed
print(req7.text)

#Beginning stage 4
stage4_dict = {'token' : token}
req8 = requests.post('http://challenge.code2040.org/api/time', data = None, json = stage4_dict)
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
#check if stage 4 passed
print(req9.text)

#Check status of API challenge
status_url = 'http://challenge.code2040.org/api/status'
req10 = requests.post(status_url, data = None, json = stage4_dict)
print(req10.text)
