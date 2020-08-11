from tkinter import *
from tkinter import filedialog, messagebox
import os
import sys
import glob

class Application:
    def __init__(self, master):
        self.master = master
        master.title("Bulk File Renamer")
        root.minsize(425, 300)

        self.menu = Menu(root)
        root.config(menu=self.menu)

        self.fileMenu = Menu(self.menu, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.progExit)
        self.menu.add_cascade(label="File", menu=self.fileMenu)

        self.helpMenu = Menu(self.menu, tearoff=0)
        self.helpMenu.add_command(label="About Me", command=self.aboutMe)
        self.helpMenu.add_command(label="Instructions", command=self.progHelp)
        self.menu.add_cascade(label="Help", menu=self.helpMenu)

        self.label1 = Label(root, text="Desired Filename")
        self.label1.grid(column=0, row=1, pady=(15, 0))

        self.entry1 = Entry(root)
        self.entry1.grid(column=0, row=2, padx=10)

        self.label2 = Label(root, text="Old Extension")
        self.label2.grid(column=1, row=1, pady=(15, 0))

        self.entry2 = Entry(root)
        self.entry2.grid(column=1, row=2, padx=10)



        self.label3 = Label(root, text="New Extension")
        self.label3.grid(column=2, row=1, pady=(15, 0))

        self.entry3 = Entry(root)
        self.entry3.grid(column=2, row=2, padx=10)

        self.button4 = Button(root, text="Choose Directory", command=self.dirChoice)
        self.button4.grid(column=0, row=5, pady=(140, 5))

        self.button5 = Button(root, text="Rename files", command=self.bulkRename)
        self.button5.grid(column=2, row=5, pady=(140, 5))

    def progExit(self):
        sys.exit(0)

    def aboutMe(self):
        messagebox.showinfo('About Me', 'Author: Isaiah Jared \n\nhttps://github.com/iljared98/', )

    def progHelp(self):
        messagebox.showinfo('Help','Using the program:\n\n1. Enter your desired name template then click Confirm.\n2. Enter the file extension you want to rename. Click Confirm\n3. Enter a new extension if you want to replace the old, if not, simply re-enter the old extension. Click Confirm.\n4. Choose your directory with the files you want to rename.\n5. "Click Rename Files"')

    def dirChoice(self):
        self.path = filedialog.askdirectory() + '/'

    def bulkRename(self):
        self.filename = self.entry1.get()
        self.oldExt = self.entry2.get()
        self.newExt = self.entry3.get()

        if "." in self.oldExt or "." in self.newExt:
            messagebox.showerror("Input Error",'Please only enter the extension name (ex. PNG).')
        else:
            if len(self.filename) == 0 or len(self.oldExt) == 0 or len(self.newExt) == 0:
                messagebox.showerror("Input Error",'One of your input fields is empty.')
            else:
                try:
                    filelist = glob.glob(self.path + "*.{}".format(self.oldExt))
                    i = 0
                    for file in filelist:
                        old_filename = os.path.split(file)
                        os.path.splitext(self.path)[0] + '{}'.format(self.oldExt)
                        new_filename = self.path + self.filename + str(i + 1) + ".{}".format(self.newExt)
                        os.rename(self.path + old_filename[1], new_filename)
                        i = i + 1

                except ValueError:
                    messagebox.showerror('Error','Please double check your inputs and try again.')
root = Tk()
my_gui = Application(root)
root.mainloop()


