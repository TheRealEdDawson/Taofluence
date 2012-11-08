import requests
import json
from requests.auth import HTTPBasicAuth
import sys
import string

#Checking that all required arguments (username and password) were passed.

<<<<<<< HEAD
if len(sys.argv) < 4:
    argumentsnotset = "\nError: one or more arguments were not passed. \n\nUsage is like so: \n\npython zen-create-post.py ZENDESKUSERNAME ZENDESKPASSWORD FORUMID"
=======
if len(sys.argv) < 3:
    argumentsnotset = "\nError: one or more arguments were not passed. \n\nUsage is like so: \n\npython taofluence.py ZENDESKUSERNAME ZENDESKPASSWORD\n" 
>>>>>>> 113dc5945024de57cc1b620ece219803d828341e
    print argumentsnotset
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
forum_id = sys.argv[3]

auth = HTTPBasicAuth(username,password)

url = 'https://ninefold.zendesk.com/api/v2/topics.json'

title_text = "Test Topic from REST"
body_text = "This is a test created via REST API."
jsonbit1 = '''{"topic": {"forum_id": '''
jsonbit2 = ''', "title": \"'''
jsonbit3 = '''\" , "body": \"''' 
jsonbit4 = '''\"}}'''

payload = jsonbit1 + forum_id + jsonbit2 + title_text + jsonbit3 + body_text + jsonbit4

data=payload

#print data , "\n" #temporary debug point
#sys.exit(1) #temporary breakpoint

headers = {'content-type': 'application/json'}

r = requests.post(url=url, auth=auth, data=data, headers=headers)
print r.text
print r.status_code
print r.headers
print r.headers['content-type']
