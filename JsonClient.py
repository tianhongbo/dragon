import json
import urllib2

TokenData = {"auth":
        {"passwordCredentials":
         {"username": "admin", "password":"password"
          },"tenantId":"f540d68440e146ed83537bb88002af16"
         }
        }
TokenData_json = json.dumps(TokenData)

HttpHeader = {'content-type': 'application/json'}
QuantumHost = "http://10.145.90.128:9696/v2.0/api"
TokenHost = "http://10.145.90.128:5000/v2.0/tokens"

#Get the token before request which will expire in 24-hours
ReqToken = urllib2.Request(TokenHost, 'POST', TokenData, HttpHeader)

#req = urllib2.Request(host, 'GET', data, {'content-type': 'application/json'})
print "the request", ReqToken.headers
#response_stream = urllib2.urlopen(ReqToken)
req = urllib2.urlopen(TokenHost)
#json_response = response_stream.read()
