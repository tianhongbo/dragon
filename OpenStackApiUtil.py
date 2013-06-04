# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created: June 3, 2013
# Updated: June 3, 2013
# Code version: 0.0.1
# Python version: 2.7.5
# Purpose: The file is the collection of OpenStack API common function
# Function:
#     1. Network Menu

import httplib
import json
import urllib

def OpenStackApiUtilGet(Token, Host, Uri):
    Headers= {"X-Auth-Token": Token, "Content-Type": "application/json"}

    # HTTP Connection
    conn = httplib.HTTPConnection(Host)
    conn.request("GET", Uri, None, Headers)

    # HTTP response
    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    # HTTP Close
    conn.close()
    return dd

def OpenStackApiUtilReqDataJson(Host, Headers, Method, Uri, Params):
    # Open HTTP Connection
    conn = httplib.HTTPConnection(Host)
    conn.request(Method, Uri, Params, Headers)

    # HTTP response
    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)

    # HTTP Close
    conn.close()

    # return the JSON data
    return dd
