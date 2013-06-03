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

def OpenStackOverviewPhyView():
    MyFile = "physical.gif"
    OpenStackDisplayMiscTopLevelPictureGif(MyFile)

def OpenStackOverviewLogicalView():
    MyFile = "logical.gif"
    OpenStackDisplayMiscTopLevelPictureGif(MyFile)

def OpenStackOverviewTopoView():
    MyFile = "Topology.gif"
    OpenStackDisplayMiscTopLevelPictureGif(MyFile)

class OpenStackOverviewMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the UseCase Menu
        self.add_command(label="Physical View", command=OpenStackOverviewPhyView)
        self.add_command(label="Logical View", command=OpenStackOverviewLogicalView)
        self.add_command(label="Topology View", command=OpenStackOverviewTopoView)
        #self.add_separator()
