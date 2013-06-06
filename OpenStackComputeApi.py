# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created: June 4, 2013
# Updated: June 4, 2013
# Code version: 0.0.1
# Python version: 2.7.5
# Purpose: It is the collection of all OpenStack Compute API V2.0
# Function:
#     1. Compute API v2.0

from OpenStackDisplayMisc import *
from OpenStackApiUtil import *
from KeyStoneToken import *

def OpenStackComputeListServers():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()

    ApiConf = OpenStackApiConf()
    myHost = ApiConf.nova_api_server
    myHeaders = Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}
    myMethod = "GET"
    myUri = "/v2/426e5b25d70d4e9c9835fab8fcb7f686/servers/detail"
    myParams = None

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["servers"]
    OpenStackDispJson(value)

def OpenStackComputeListImages():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    ApiConf = OpenStackApiConf()
    myHost = ApiConf.nova_api_server

    myHeaders = Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}
    myMethod = "GET"
    myUri = "/v2/426e5b25d70d4e9c9835fab8fcb7f686/images/detail"
    myParams = None

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["images"]
    OpenStackDispJson(value)

def OpenStackComputeListFlavors():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    ApiConf = OpenStackApiConf()
    myHost = ApiConf.nova_api_server

    myHeaders = Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}
    myMethod = "GET"
    myUri = "/v2/426e5b25d70d4e9c9835fab8fcb7f686/flavors"
    myParams = None

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["flavors"]
    OpenStackDispJson(value)
