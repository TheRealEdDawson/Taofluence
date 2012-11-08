import requests
import json
from requests.auth import HTTPBasicAuth
import sys

#Checking that all required arguments (username and password) were passed.

if len(sys.argv) < 3:
    argumentsnotset = "\nError: one or more arguments were not passed. \n\nUsage is like so: \n\npython taofluence.py ZENDESKUSERNAME ZENDESKPASSWORD\n" 
    print argumentsnotset
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

auth = HTTPBasicAuth(username,password)

url = 'https://ninefold.zendesk.com/api/v2/topics.json'

payload = {"topic": {"forum_id": 21371187, "title": "Test Announcement Topic from REST", "body": "This is a test created via REST API."}}

data=json.dumps(payload)

headers = {'content-type': 'application/json'}

r = requests.post(url=url, auth=auth, data=data, headers=headers)
print r.text
print r.status_code
print r.headers
print r.headers['content-type']
