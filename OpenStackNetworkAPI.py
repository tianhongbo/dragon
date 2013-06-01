# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created: May 31, 2013
# Updated: May 31, 2013
# Code version: 0.0.1
# Python version: 2.7.5
# Purpose: Implement OpenStack Network API V2.0
# Function:
#     1. Network API v2.0

import httplib
import json
import urllib
import pprint

def OpenStackNetworkApiGet(TempToken):
    
    ## List the networks configured in Quantum by user - Admin
    # QuantumHost = "http://10.145.90.128:9696/v2.0/api/"
    # arguments
    urlQuantum = "10.145.90.128:9696"
    headersQuantum = {"X-Auth-Token": TempToken, "Content-Type": "application/json"}

    # HTTP Connection
    connQuantum = httplib.HTTPConnection(urlQuantum)
    connQuantum.request("GET", "/v2.0/networks", None, headersQuantum)

    # HTTP response
    responseQuantum = connQuantum.getresponse()
    dataQuantum = responseQuantum.read()
    ddQuantum = json.loads(dataQuantum)

    # HTTP Close
    connQuantum.close()
    return ddQuantum
