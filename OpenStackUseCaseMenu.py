# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created: June 3, 2013
# Updated: June 3, 2013
# Code version: 0.0.1
# Python version: 2.7.5
# Purpose: The collection of all the use case for CloudEPC and OpenStack API
# Function:
#     1. 1 - Cluster
#     2. 2 - 

from Tkinter import *
from OpenStackDisplayMisc import *

def OpenStackUseCaseDisplay():
    # Obtain the Token from KeyStone
    pass

class OpenStackUseCaseMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the UseCase Menu
        self.add_command(label="1. Boot-up with Auto-config", command=OpenStackUseCaseDisplay)
        self.add_command(label="2. Create One CP per Host", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="3. Create Multi-cluster for EPC", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="4. Compute Resource Scheduling Policy", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="5. Automation", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="6. Live Migration", command=OpenStackDisplayMiscTopLevelMessage)
        #self.add_separator()
