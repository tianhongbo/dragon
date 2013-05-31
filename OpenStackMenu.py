# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Compute
#     2. Network
#     3. Storage
#     4. Identity
#     5. Exit

from Tkinter import *
from OpenStackComputeMenu import *
from OpenStackNetworkMenu import *
from OpenStackStorageMenu import *
from OpenStackIdentityMenu import *


# define stub func
def callback():
    print "It is comming soon..."

class OpenStackMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Compute Menu
        ComputeMenu = OpenStackComputeMenu(self)
        self.add_cascade(label="Compute", menu=ComputeMenu)

        # Create the Network Menu
        NetworkMenu = OpenStackNetworkMenu(self)
        self.add_cascade(label="Network", menu=NetworkMenu)

        # Create the Storage Menu
        StorageMenu = OpenStackStorageMenu(self)
        self.add_cascade(label="Storage", menu=StorageMenu)

        # Create the Identity Menu
        IdentityMenu = OpenStackIdentityMenu(self)
        self.add_cascade(label="Identity", menu=IdentityMenu)

        # Create the Exit Menu
        ExitMenu = Menu(self)
        self.add_cascade(label="Exit", command=self.quit)  
