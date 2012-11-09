import requests
import json
from requests.auth import HTTPBasicAuth
import sys
import string
import datetime
from xmlrpclib import ServerProxy as Server

#Checking that all required command-line arguments (username and password) were passed.

if len(sys.argv) < 8:
    argumentsnotset = "\nError: one or more arguments were not passed. \n\nUsage is like so: \
    \n\npython zen-create-post.py ZENDESKURL ZENDESKUSERNAME ZENDESKPASSWORD ZENDESKFORUMID \
    CONFLUENCEURL CONFLUENCEUSERNAME CONFLUENCEPASSWORD CONFLUENCESPACE"
    print argumentsnotset
    sys.exit(1)

zendesk_url = sys.argv[1]
# The REST access point for creating topics in Zendesk is 'https://YOURDOMAIN.zendesk.com/api/v2/topics.json'
zendesk_username = sys.argv[2]
zendesk_password = sys.argv[3]
zendesk_forum_id = sys.argv[4]

# Setting Confluence URL, Space, username and password. Note confluence_server requires a https URL.
confluence_server_url = sys.argv[5]
conf_user = sys.argv[6]
conf_pwd = sys.argv[7]
conf_space = sys.argv[8]

# Access the Confluence site via XML-RPC to retrieve the list of all pages in the space (once-off)
s = Server(confluence_server_url + "/rpc/xmlrpc")
s = s.confluence1
confluence_token = s.login(conf_user,conf_pwd)
# this is a "dictionary" (spaceindex)
confluence_spaceindex = s.getPages(confluence_token, conf_space)
print confluence_spaceindex #temporary debug point
s.logout(confluence_token)

#Set up Zendesk login credentials from command-line arguments
zendesk_auth = HTTPBasicAuth(zendesk_username,zendesk_password)

#define dynamic content to go into the Zendesk page
time_now =str(datetime.datetime.now())
zendesk_title_text = "Test Topic from REST " + time_now
zendesk_body_text = "This is a test created via REST API at " + time_now

#build the JSON request that will be passed via REST
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
