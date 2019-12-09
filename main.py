# Author      : Isaiah Jared
# Description : Bulk renames all files with a certain
#               extension via a set pattern. User will
#               enter a base name string which will
#               then be incremented (i.e. myimage1.png, myimage2.png)
#               for each file of the same type in the directory.

from tkinter import *
from tkinter import filedialog, messagebox
import os
import sys
import glob

window = Tk()
window.title("Bulk File Renamer")
window.minsize(425,300)



# FILENAME

def storeVal1():
  global val1
  val1 = entry1.get()

# OLD EXTENSION
def storeVal2():
  global val2
  val2 = entry2.get()

# NEW EXTENSION (OVERWRITES OLD!)
def storeVal3():
  global val3
  val3 = entry3.get()

def dirChoice():
  global path
  path = filedialog.askdirectory() + '/'

def progExit():
    sys.exit(0)

def aboutMe():
    messagebox.showinfo('About Me', 'Author: Isaiah Jared \n\nhttps://github.com/iljared98/', )

def progHelp():
    messagebox.showinfo('Help','Using the program:\n\n1. Enter your desired name template then click Confirm.\n2. Enter the file extension (no .) you want to rename. Click Confirm\n3. Enter a new extension if you want to replace the old, if not, simply re-enter the old extension. Click Confirm.\n4. Choose your directory with the files you want to rename.\n5. "Click Rename Files"')


def bulkRename():
  filelist = glob.glob(path + "*.{}".format(val2))
  count = 0
  for file in filelist:
      filename = os.path.split(file)
      os.path.splitext(path)[0]+'{}'.format(val2)
      new_filename = path + val1 + str(count + 1) + ".{}".format(val3)
      os.rename(path+filename[1], new_filename)
      count = count + 1




# Menu bar #

menu = Menu(window)
window.config(menu=menu)

fileMenu = Menu(menu,tearoff=0)
fileMenu.add_command(label="Exit",command=progExit)
menu.add_cascade(label="File",menu=fileMenu)

helpMenu = Menu(menu,tearoff=0)
helpMenu.add_command(label="About Me",command=aboutMe)
helpMenu.add_command(label="Instructions",command=progHelp)
menu.add_cascade(label="Help",menu=helpMenu)

##############################################################
##############################################################

label1 = Label(window, text="Desired Filename")
label1.grid(column=0, row=1,pady=(15,0))
#label1.pack()

entry1 = Entry(window)
entry1.grid(column=0, row=2,padx=10)
#entry1.pack()

button1 = Button(window, text="Confirm",command=storeVal1)
button1.grid(column=0, row=3)
#button1.pack()

label2 = Label(window, text="Old Extension")
label2.grid(column=1, row=1,pady=(15,0))
#label2.pack()


entry2 = Entry(window)
entry2.grid(column=1, row=2,padx=10)
#entry2.pack()

button2 = Button(window, text="Confirm",command=storeVal2)
button2.grid(column=1, row=3)
#button2.pack()

label3 = Label(window, text="New Extension")
label3.grid(column=2, row=1,pady=(15,0))
#label3.pack()

entry3 = Entry(window)
entry3.grid(column=2, row=2,padx=10)
#entry3.pack()

button3 = Button(window, text="Confirm",command=storeVal3)
button3.grid(column=2, row=3)
#button3.pack()



# Change this to a folder icon or something later on

button4 = Button(window, text="Choose Directory", command=dirChoice)
button4.grid(column=0, row=5,pady=(140,5))
#button4.pack()

button5 = Button(window, text="Rename files",command=bulkRename)
button5.grid(column=2, row=5,pady=(140,5))
#button5.pack()

window.mainloop()
