# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Storage

from Tkinter import *
from OpenStackDisplayMisc import *

class OpenStackStorageMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Storage Menu
        self.add_command(label="Block Storage", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Oject Storage", command=OpenStackDisplayMiscTopLevelMessage)
