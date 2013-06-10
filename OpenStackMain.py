# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created Date: May 30, 2013
# Updated Date: May 30, 2013
# Version: 1.0.0
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Main Entrance

from Tkinter import *
from OpenStackMenu import *
from OpenStackApiUtil import *

# Define the OpenStack API Main
class OpenStackApiMain(Tk):
    def __init__(self):
        Tk.__init__(self)
        TopMenu = OpenStackMenu(self)
        self.title("CloudEPC - H.V.K")
        self.minsize(1056,600)
        #self.geometry("1000x500")
        self.config(menu=TopMenu)
        
# Main()
if __name__ == "__main__":
    # Initial the configuration data
    ApiConf = OpenStackApiConf()
    
    app=OpenStackApiMain()
    app.mainloop()
