# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created: May 31, 2013
# Updated: May 31, 2013
# Code version: 0.0.1
# Python version: 2.7.5
# Purpose: Implement OpenStack Network API V2.0
# Function:
#     1. Network API v2.0

from OpenStackDisplayMisc import *
from OpenStackApiUtil import *
from KeyStoneToken import *

def OpenStackNetworkListNetworks():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    # Get the all the Networks via Open Stack Network API v2.0
    ApiConf = OpenStackApiConf()
    Host = ApiConf.get_quantum_api_server()

    Uri = "/v2.0/networks"
    NetworksList = OpenStackApiUtilGet(Token, Host, Uri)
    
    # Format the Data to More Human readable
    SourceData = NetworksList["networks"]
    OpenStackDispJson(SourceData)

def OpenStackNetworkListSubnetworks():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    # Get the all the Sub Networks via Open Stack Network API v2.0
    ApiConf = OpenStackApiConf()
    Host = ApiConf.get_quantum_api_server()

    Uri = "/v2.0/subnets.json"
    NetworksList = OpenStackApiUtilGet(Token, Host, Uri)
    
    # Format the Data to More Human readable
    SourceData = NetworksList["subnets"]
    OpenStackDispJson(SourceData)
    
def OpenStackNetworkListPorts():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    # Get the all the Ports via Open Stack Network API v2.0
    ApiConf = OpenStackApiConf()
    Host = ApiConf.get_quantum_api_server()

    Uri = "/v2.0/ports.json"
    NetworksList = OpenStackApiUtilGet(Token, Host, Uri)
    
    # Format the Data to More Human readable
    SourceData = NetworksList["ports"]
    OpenStackDispJson(SourceData)
