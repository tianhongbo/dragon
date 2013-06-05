# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Compute

from Tkinter import *
from OpenStackDisplayMisc import *
from OpenStackComputeApi import *

class OpenStackComputeMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Compute Menu
        self.add_command(label="List Server", command=OpenStackComputeListServers)
        self.add_command(label="Show Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Creat Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Update Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="List Server Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Show Server Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Set Server Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Update Server Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete Server Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_separator()
        self.add_command(label="List Image", command=OpenStackComputeListImages)
        self.add_command(label="Show Image", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete Image", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="List Image Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Show Image Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Set Image Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Update Image Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Delete Image Metadata", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_separator()
        self.add_command(label="List Flavor", command=OpenStackComputeListFlavors)
        self.add_command(label="Show Flavor", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_separator()
        self.add_command(label="Extension-Pause Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Unpause Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Suspend Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Resume Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Migrate Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Reset Net Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Inject Net Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Lock Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Unlock Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Back-up Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Live-Migrate Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Reset Server", command=OpenStackDisplayMiscTopLevelMessage)
        self.add_command(label="Extension-Evacuate Server", command=OpenStackDisplayMiscTopLevelMessage)
