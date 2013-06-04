# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created Date: June 4, 2013
# Updated Date: June 4, 2013
# Python version: 2.7.5
# Purpose: It is the collection of all Identity API
# Function:
#     1. Identity

from Tkinter import *
from KeyStoneToken import *
from OpenStackDisplayMisc import *

# Obtain Token and display
def OpenStackIdentityApiGetToken():
    # All the arguments for user - Admin
    # If you want to change to another user, please modify the self.params
    Url = "10.145.90.128:5000"
    Params = '{"auth":{"passwordCredentials":{"username":"admin", "password":"password"},"tenantId":"f540d68440e146ed83537bb88002af16"}}'
    Headers = {"Content-Type": "application/json"}
    
    # HTTP connetion
    conn = httplib.HTTPConnection(Url)
    conn.request("POST", "/v2.0/tokens", Params, Headers)
    
    # HTTP response
    response = conn.getresponse()
    data = response.read()
    dd = json.loads(data)
    
    # HTTP close
    conn.close()
    
    # Display the token
    value = dd["access"]["token"]["id"]
    OpenStackDisplayMiscTopLevelMessage(value)

class OpenStackIdentityMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Identity Menu
        self.add_command(label="Token", command=OpenStackIdentityGetToken)
        self.add_command(label="Tenant", command=OpenStackDisplayMiscTopLevelMessage)
