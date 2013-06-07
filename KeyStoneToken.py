# Before you access any OpenStack API, you should obtain the token from KeyStone.
# This class is that Using Python to Obtain the Authentication Token.
# This token you got will expire in 24 hours which you need to consider.
# The following are the auth information:
# export OS_TENANT_NAME=admin
# export OS_USERNAME=admin
# export OS_PASSWORD=password
# export OS_AUTH_URL="http://localhost:5000/v2.0/"
# export SERVICE_ENDPOINT="http://localhost:35357/v2.0"
# export SERVICE_TOKEN=password

import httplib
import json
import urllib
from OpenStackApiUtil import *


class KeyStoneToken:

    # Token value, initiled with none
    Token = ''
    HttpUrl = ''
    HttpParams = ''
    HttpHeaders = ''

    def __init__(self):
        # All the arguments for user - Admin
        # If you want to change to another user, please modify the self.params
        ApiConf = OpenStackApiConf()
        self.HttpUrl = ApiConf.get_keystone_api_server()
        
        self.HttpParams = '{"auth":{"passwordCredentials":{"username":"demo", "password":"password"},"tenantId":"426e5b25d70d4e9c9835fab8fcb7f686"}}'
        self.HttpHeaders = {"Content-Type": "application/json"}
        
    # Method to obtain the token from KeyStone
    def GetToken(self):
        
        # HTTP connetion
        conn = httplib.HTTPConnection(self.HttpUrl)
        conn.request("POST", "/v2.0/tokens", self.HttpParams, self.HttpHeaders)
        
        # HTTP response
        response = conn.getresponse()
        data = response.read()
        dd = json.loads(data)
        # HTTP close
        conn.close()
        
        # Display the token
        self.value = dd['access']['token']['id']
        return self.value
