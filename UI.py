from tkinter import *
from Search import  *

class UI:
    def __init__(self, master):
        master.minsize(width=666, height=666)
        master.maxsize(width=666, height=666)
        master.grid_columnconfigure(0, weight=1)
        self.scrollbar = Scrollbar(master, orient=VERTICAL)
        v = StringVar()
        self.directoryEntry = Entry(master,textvariable=v)
        self.directoryEntry.grid(row=0,sticky=N+S+E+W)

        self.directoryEntryButton = Button(master,text='OK', command=self.saveEntry)
        self.directoryEntryButton.grid(row=0,column=1,sticky=N+S+E+W)

        self.list = Listbox(master,yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list.yview)
        self.scrollbar.grid(row=1,column=1,rowspan=2,sticky=N+S+E+W)
        self.list.grid(row=1,rowspan=2,sticky=N+S+E+W)
        self.list.bind('<Double-Button-1>', self.OnDouble)

        mainDir = v.get()









    def saveEntry(self):
        self.list.delete(0,END)
        entry = self.directoryEntry.get()
        self.directoryEntry.delete(0, END)
        lst = findDirectories(['.txt','.yml', '.lua'],entry)
        for item in lst:
            self.list.insert(END, item)

    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        click_on_file(value)






def start():
    root = Tk()
    start = AskDir(root)
    root.mainloop()