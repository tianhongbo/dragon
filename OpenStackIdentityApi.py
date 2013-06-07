# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created Date: June 4, 2013
# Updated Date: June 4, 2013
# Version: 0.0.2
# Python version: 2.7.5
# Purpose: It is the collection of all Identity API
# Function:
#     1. Identity

from Tkinter import *
from KeyStoneToken import *
from OpenStackDisplayMisc import *
from OpenStackApiUtil import *

# Obtain Token and display
def OpenStackIdentityApiGetToken():
    
    ApiConf = OpenStackApiConf()
    myHost = ApiConf.get_keystone_api_server()

    myHeaders = {"Content-Type": "application/json"}
    myMethod = "POST"
    myUri = "/v2.0/tokens"
    myParams = '{"auth":{"passwordCredentials":{"username":"admin", "password":"password"},"tenantId":"f540d68440e146ed83537bb88002af16"}}'

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["access"]["token"]["id"]
    OpenStackDisplayMiscTopLevelMessage(value)
    
def OpenStackIdentityApiListTenants():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    ApiConf = OpenStackApiConf()
    myHost = ApiConf.get_keystone_api_server()

    myHeaders = Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}
    myMethod = "GET"
    myUri = "/v2.0/tenants"
    myParams = None

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["tenants"]
    OpenStackDispJson(value)
    

def OpenStackIdentityApiListUsers():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    ApiConf = OpenStackApiConf()
    myHost = ApiConf.get_admin_api_server()

    myHeaders = Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}
    myMethod = "GET"
    myUri = "/v2.0/users"
    myParams = None

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["users"]
    OpenStackDispJson(value)
