# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Identity

from Tkinter import *
from KeyStoneToken import *
from OpenStackDisplayMisc import *

# Obtain Token and display
def OpenStackIdentityGetToken():
    # Get the Token
    MyToken = KeyStoneToken()
    Token = MyToken.GetToken()

    # Dispaly the Token
    OpenStackDisplayMiscTopLevelMessage("Your Token is:\n "+Token)

class OpenStackIdentityMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Identity Menu
        self.add_command(label="Token", command=OpenStackIdentityGetToken)
        self.add_command(label="Tenant", command=OpenStackDisplayMiscTopLevelMessage)
