# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created: May 30, 2013
# Updated: May 31, 2013
# Code version: 0.0.1
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Network Menu

from Tkinter import *
from OpenStackDisplayMisc import *
from OpenStackNetworkAPI import *
from KeyStoneToken import *

def OpenStackNetworkListNetworks():
    # Obtain the Token from KeyStone
    TempToken = KeyStoneToken()
    Token = TempToken.GetToken()
    
    # Get the all the Networks via Open Stack Network API v2.0
    NetworksList = OpenStackNetworkApiGet(Token)

    # Format the Data to More Human readable
    SourceData = NetworksList["networks"]
    OpenStackDispJson(SourceData)

class OpenStackNetworkMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Network Menu
        self.add_command(label="List Networks", command=OpenStackNetworkListNetworks)
        self.add_command(label="Show Networks", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Create Networks", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Update Networks", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete Networks", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_separator()
        self.add_command(label="List Subnets", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Show Subnets", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Create Subnets", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Update Subnets", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete Subnets", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_separator()
        self.add_command(label="List Ports", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Show Ports", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Create Ports", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Update Ports", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete ports", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_separator()
        self.add_command(label="List Extension", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Provider Network Extension", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Layer-3 Network Extension", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="ExtraRoute Extension", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Load Balancer Extension", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Security Group and Rule", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Agent Management Extension", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Agent Scheduller Extension", command=OpenStackDisplayMiscTopLevelMessage)
        
        

