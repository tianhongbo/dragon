# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Storage

from Tkinter import *

# define stub func
def callback3():
    print "Storage is comming soon..."

class OpenStackStorageMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Storage Menu
        self.add_command(label="Block Storage", command=callback3)
        self.add_command(label="Oject Storage", command=callback3)
