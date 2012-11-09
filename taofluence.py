import requests
import json
from requests.auth import HTTPBasicAuth
import sys
import string
import datetime

#Checking that all required arguments (username and password) were passed.

if len(sys.argv) < 4:
    argumentsnotset = "\nError: one or more arguments were not passed. \n\nUsage is like so: \n\npython zen-create-post.py ZENDESKUSERNAME ZENDESKPASSWORD FORUMID"
    print argumentsnotset
    sys.exit(1)

zendesk_username = sys.argv[1]
zendesk_password = sys.argv[2]
zendesk_forum_id = sys.argv[3]
zendesk_url = sys.argv[4]
# The REST access point for creating topics in Zendesk is 'https://ninefold.zendesk.com/api/v2/topics.json'

#Set up login credentials from command-line arguments
zendesk_auth = HTTPBasicAuth(zendesk_username,zendesk_password)

#define dymanic content to go into the page
time_now =str(datetime.datetime.now())
zendesk_title_text = "Test Topic from REST " + time_now
zendesk_body_text = "This is a test created via REST API at " + time_now

jsonbit1 = '''{"topic": {"forum_id": '''
jsonbit2 = ''', "title": \"'''
jsonbit3 = '''\" , "body": \"''' 
jsonbit4 = '''\"}}'''

payload = jsonbit1 + zendesk_forum_id + jsonbit2 + zendesk_title_text + jsonbit3 + zendesk_body_text + jsonbit4
zendesk_data=payload

#print data , "\n" #temporary debug point
#sys.exit(1) #temporary breakpoint

zendesk_headers = {'content-type': 'application/json'}

r = requests.post(url=zendesk_url, auth=zendesk_auth, data=zendesk_data, headers=zendesk_headers)
print r.text
print r.status_code
print r.headers
print r.headers['content-type']
