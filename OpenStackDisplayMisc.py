# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 31, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Display Tool

from Tkinter import *

def OpenStackDisplayMiscTopLevelMessage(MessageStr="It is comming soon..."):
    # Dispaly the Message
    MyWindow = Toplevel()
    MyWindow.title("CloudEPC")
    MyWindow.minsize(320,180)
    w = Label(MyWindow, justify=LEFT, text=MessageStr)
    w.pack()
    MyWindow.mainloop()
