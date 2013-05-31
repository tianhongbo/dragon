# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Network

from Tkinter import *

# define stub func
def callback2():
    print "Network is coming soon..."

class OpenStackNetworkMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Network Menu
        self.add_command(label="Network", command=callback2)
        self.add_command(label="Subnet", command=callback2)
        self.add_command(label="Port", command=callback2)
        self.add_command(label="Extension", command=callback2)

