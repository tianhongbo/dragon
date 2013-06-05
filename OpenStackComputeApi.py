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
    
    myHost = "10.145.90.128:8774"
    myHeaders = Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}
    myMethod = "GET"
    myUri = "/v2/f540d68440e146ed83537bb88002af16/servers/detail"
    myParams = None

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["servers"]
    OpenStackDispJson(value)

def OpenStackComputeListImages():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    myHost = "10.145.90.128:8774"
    myHeaders = Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}
    myMethod = "GET"
    myUri = "/v2/f540d68440e146ed83537bb88002af16/images/detail"
    myParams = None

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["images"]
    OpenStackDispJson(value)

def OpenStackComputeListFlavors():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    myHost = "10.145.90.128:8774"
    myHeaders = Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}
    myMethod = "GET"
    myUri = "/v2/f540d68440e146ed83537bb88002af16/flavors"
    myParams = None

    dd = OpenStackApiUtilReqDataJson(myHost, myHeaders, myMethod, myUri, myParams)

    # Display the token
    value = dd["flavors"]
    OpenStackDispJson(value)
