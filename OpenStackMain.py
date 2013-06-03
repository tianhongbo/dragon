# Author: Hongbo Tian / tianhongbo1@gmail.com
# Date: May 30, 2013
# Python version: 2.7.5
# Purpose: Demo show the function list of OpenStack API
# Function:
#     1. Main Entrance

from Tkinter import *
from OpenStackMenu import *

# Define the OpenStack API Main
class OpenStackApiMain(Tk):
    def __init__(self):
        Tk.__init__(self)
        TopMenu = OpenStackMenu(self)
        self.title("CloudEPC")
        self.minsize(1056,600)
        #self.geometry("1000x500")
        self.config(menu=TopMenu)

        # create the mLAB picture as the main windows background
        canvas = Canvas(self, width = 300, height = 200)
        photo = PhotoImage(file="mlab.gif")
        item = canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.pack(expand = YES, fill = BOTH)
        canvas.mainloop()
        
# Main()
if __name__ == "__main__":
    app=OpenStackApiMain()
    app.mainloop()
