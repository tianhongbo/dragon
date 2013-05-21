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
# QuantumHost = "http://10.145.90.128:9696/v2.0/api/"

import httplib
import json
import urllib
import pprint

## Obtain the token from KeyStone for user - admin
# arguments
url = "10.145.90.128:5000"
params = '{"auth":{"passwordCredentials":{"username":"admin", "password":"password"},"tenantId":"f540d68440e146ed83537bb88002af16"}}'
headers = {"Content-Type": "application/json"}

# HTTP connetion
conn = httplib.HTTPConnection(url)
conn.request("POST", "/v2.0/tokens", params, headers)

# HTTP response
response = conn.getresponse()
data = response.read()
dd = json.loads(data)

# HTTP close
conn.close()

# Display the token
apitoken = dd['access']['token']['id']
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
conn.close()

# Display the data
print "This is the original data:", ddQuantum

print "------------------------"
for i in ddQuantum['networks']:
    print "record: ", i

print "*************************"
pprint.pprint(ddQuantum)
