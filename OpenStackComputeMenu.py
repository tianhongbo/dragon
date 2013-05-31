# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Compute

from Tkinter import *

# define stub func
def callback1():
    print "Compute is comming soon..."

class OpenStackComputeMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Compute Menu
        self.add_command(label="Server", command=callback1)
        self.add_command(label="Image", command=callback1)
        self.add_command(label="Flavor", command=callback1)
        self.add_command(label="Extension", command=callback1)
        self.add_command(label="Misc", command=callback1)
