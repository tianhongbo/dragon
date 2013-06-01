# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Compute

from Tkinter import *
from OpenStackDisplayMisc import *

class OpenStackComputeMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Compute Menu
        self.add_command(label="Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Image", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Flavor", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Misc", command=OpenStackDisplayMiscTopLevelMessage)
