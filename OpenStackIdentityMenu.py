# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Identity

from Tkinter import *
from KeyStoneToken import *
from OpenStackDisplayMisc import *
from OpenStackIdentityApi import *

class OpenStackIdentityMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Identity Menu
        self.add_command(label="Get Token", command=OpenStackIdentityApiGetToken)
        self.add_command(label="Validate Token", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Check Token", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="List Endpoints of Token", command=OpenStackDisplayMiscTopLevelMessage)
        
        self.add_separator()
        self.add_command(label="List Tenants", command=OpenStackIdentityApiListTenants)
        self.add_command(label="Add Tenants", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Update Tenants", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete Tenants", command=OpenStackDisplayMiscTopLevelMessage)

        self.add_separator()
        self.add_command(label="List Users", command=OpenStackIdentityApiListUsers)
        self.add_command(label="Add Users", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Update Users", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete Users", command=OpenStackDisplayMiscTopLevelMessage)
