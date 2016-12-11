from tkinter import *
from Search import  *
class UI:
    def __init__(self, master):

        self.directoryEntry = Entry(master)
        self.directoryEntry.grid(row=0, column=0, sticky=W)

        self.directoryEntryButton = Button(master,text='OK', command=self.saveEntry)
        self.directoryEntryButton.grid(row=0, column=1, sticky=W)

        self.list = Listbox(master)
        self.list.grid(row=1)


    def saveEntry(self):
        self.entry = self.directoryEntry.get()
        self.directoryEntry.delete(0, END)
        







def start():
    root = Tk()
    test = UI(root)
    root.mainloop()