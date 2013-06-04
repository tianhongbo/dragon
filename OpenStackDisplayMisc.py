# Author: Hongbo Tian / tianhongbo1@gmail.com
# Created Date: May 31, 2013
# Updated Date: June 3, 2013
# Version: 0.0.2
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Display the message in the toplevel window
#     2. Display the picture in the toplevel window

from Tkinter import *
import json

# Display the message in the toplevel window
def OpenStackDisplayMiscTopLevelMessage(MessageStr="It's comming soon! We are working on that..."):
    # Create the toplevel window
    MyWindow = Toplevel()
    MyWindow.title("CloudEPC")
    MyWindow.minsize(320,240)

    # Read the team photo from the file as the bacground
    MyPhoto = PhotoImage(file="mteam.gif")
    
    # Create the Canvas in the toplevel window
    MyCanvas = Canvas(MyWindow, width = 320, height = 240)
    MyItem = MyCanvas.create_image(0, 0, anchor=NW, image=MyPhoto)
    MyCanvas.pack(expand = YES, fill = BOTH)

    # create the label in the toplevel window
    w = Label(MyWindow, justify=LEFT, text=MessageStr)
    w.pack()

    MyWindow.mainloop()

# Display the picture in the toplevel window
# Currently only can support the .gif format in order to simple the code
# otherwise you need install the PIL moudle.
def OpenStackDisplayMiscTopLevelPictureGif(PictureFileName=""):
    # Read the Picture from the file
    MyPhoto = PhotoImage(file=PictureFileName)

    # Create the toplevel window
    MyWindow = Toplevel()
    MyWindow.title("CloudEPC")
    MyWindow.minsize(640,640)

    # Create the Canvas in the toplevel window
    MyCanvas = Canvas(MyWindow, width = 640, height = 640)
    MyItem = MyCanvas.create_image(0, 0, anchor=NW, image=MyPhoto)
    MyCanvas.pack(expand = YES, fill = BOTH)
    MyWindow.mainloop()

def OpenStackDispJson(SourceData):
    # Create the toplevel window
    MyWindow = Toplevel()
    MyWindow.title("CloudEPC")
    MyWindow.minsize(640,360)

    # Format the Data to More Human readable
    x = 0
    for z in SourceData:
        y = 0
        for MyNetwork in z:
            # Print the Clomun 0 as the title if x == 0
            if x is 0:
                Label(MyWindow, text=MyNetwork, borderwidth=2, relief=GROOVE).grid(row=y, column=0, sticky=W, padx=5, pady=5)

            Label(MyWindow, text=z[MyNetwork], borderwidth=2, relief=GROOVE).grid(row=y, column=x+1, sticky=W, padx=5, pady=5)
            y = y + 1
        x = x + 1

    if x is 0:
        Label(MyWindow, text="There is no Data")
    MyWindow.mainloop()
