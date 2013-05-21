import json
import urllib2

# The following are the auth information
# export OS_TENANT_NAME=admin
# export OS_USERNAME=admin
# export OS_PASSWORD=password
# export OS_AUTH_URL="http://localhost:5000/v2.0/"
# export SERVICE_ENDPOINT="http://localhost:35357/v2.0"
# export SERVICE_TOKEN=password

TokenData = { "auth":{ "passwordCredentials":{ "username":"test_user",
"password":"mypass" }, "tenantName":"customer-x" } }
HttpHeader = {'content-type': 'application/json'}
QuantumHost = "http://10.145.90.128:9696/v2.0/api/"
TokenHost = "https://10.145.90.128:5000/v2.0/tokens/"

print TokenData
TokenData_json = json.dumps(TokenData)
print TokenData_json

#Get the token before request which will expire in 24-hours
ReqToken = urllib2.Request(TokenHost+'POST', TokenData_json, HttpHeader)

#req = urllib2.Request(host, 'GET', TokenData_json, {'content-type': 'application/json'})
print "the request", ReqToken.get_full_url

response_stream = urllib2.urlopen(ReqToken)
print "url open", ReqToken

json_response = response_stream.read()
print "respone...",json_response

