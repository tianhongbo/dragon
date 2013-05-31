# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Identity

from Tkinter import *
from KeyStoneToken import *

# define stub func
def callback4():
    print "Identity is comming soon..."

# define func() to obtain Token and display
def OpenStackIdentityGetToken():
    Token = KeyStoneToken()
    Token.GetToken()
    apitoken = Token.value
    print "Your token is: %s" % apitoken
    MyWindow = Toplevel()
    MyWindow.title("congratulations!")
    w = Label(MyWindow, text="Your Token is: "+apitoken)
    w.pack()
    MyWindow.mainloop()

class OpenStackIdentityMenu(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)

        # Create the Identity Menu
        self.add_command(label="Token", command=OpenStackIdentityGetToken)
        self.add_command(label="Tenant", command=callback4)
