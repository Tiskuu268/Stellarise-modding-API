from tkinter import *
from Search import *

class UI:
    def __init__(self, master):
        master.minsize(width=666, height=666)
        master.maxsize(width=666, height=666)
        master.grid_columnconfigure(0, weight=1)
        self.scrollbar1 = Scrollbar(master, orient=VERTICAL)
        self.scrollbar2 = Scrollbar(master, orient=VERTICAL)

        self.directoryEntry = Entry(master)
        self.directoryEntry.grid(row=0,sticky=EW)

        self.directoryEntryButton = Button(master,text='OK', command=self.saveEntry)
        self.directoryEntryButton.grid(row=0,column=1,sticky=EW)

        self.list = Listbox(master,yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.list.yview)
        self.scrollbar1.grid(row=1,column=1,rowspan=2,sticky=N+S+E+W)
        self.list.grid(row=1,rowspan=2,sticky=N+S+E+W)
        self.list.bind('<Double-Button-1>', self.OnDouble)


        self.directoryEntrySearch = Entry(master)
        self.directoryEntrySearch.grid(row=3, sticky=EW)

        self.directorySearchButton = Button(master, text='OK', command=self.activate_search)
        self.directorySearchButton.grid(row=3, column=1, sticky=EW)

        self.search = Listbox(master, yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.search.yview)
        self.scrollbar2.grid(row=4, column=1, rowspan=2, sticky=N + S + E + W)
        self.search.grid(row=4, rowspan=2, sticky=N + S + E + W)
        self.search.bind('<Double-Button-1>', self.OnDouble)


    def saveEntry(self):
        self.list.delete(0,END)
        entry = self.directoryEntry.get()
        self.directoryEntry.delete(0, END)
        lst = findDirectories(['.txt','.yml', '.lua'],entry)
        for item in lst:
            self.list.insert(END, item)

    def activate_search(self):
        self.search.delete(0,END)
        entry = self.directoryEntrySearch.get()
        self.directoryEntrySearch.delete(0, END)
        lst = search(['.txt','.yml', '.lua'], "C:\Program Files (x86)\Steam\steamapps\common\Stellaris", entry)
        for item in lst:
            self.search.insert(END, item)


    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        click_on_file(value)






def start():
    root = Tk()
    start = UI(root)
    root.mainloop()