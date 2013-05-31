# This function will call the quantum API# 
# QuantumHost = "http://10.145.90.128:9696/v2.0/api/"

import httplib
import json
import urllib
import pprint
from KeyStoneToken import *

# Get the token from keystone via API
Token = KeyStoneToken()
Token.GetToken()
apitoken = Token.value
print "Your token is: %s" % apitoken

## List the networks configured in Quantum by user - Admin
# arguments
urlQuantum = "10.145.90.128:9696"
headersQuantum = {"X-Auth-Token": apitoken, "Content-Type": "application/json"}

# HTTP Connection
connQuantum = httplib.HTTPConnection(urlQuantum)
connQuantum.request("GET", "/v2.0/networks", None, headersQuantum)

# HTTP response
responseQuantum = connQuantum.getresponse()
dataQuantum = responseQuantum.read()
ddQuantum = json.loads(dataQuantum)

# HTTP Close
connQuantum.close()

# Display the data
print "This is the original data:", ddQuantum

print "------------------------"
for i in ddQuantum['networks']:
    print "record: ", i



print "*************************"
print json.dumps(ddQuantum, indent=2)
