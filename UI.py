from tkinter import filedialog
from tkinter import *
from Search import *

class UI:
    def __init__(self, master):
        # Window Size
        self.master = master
        self.master.minsize(width=1080, height=720)
        self.master.maxsize(width=1080, height=720)
        self.master.grid_columnconfigure(0, weight=1)

        # ScrollBars
        self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
        self.scrollbar2 = Scrollbar(self.master, orient=VERTICAL)
        self.scrollbar3 = Scrollbar(self.master, orient=VERTICAL)

        # Labels
        self.directoryLabel = Label(self.master, text='Insert Stellaris folder directory')
        self.directoryLabel.grid(row=0, sticky=EW)

        # Directory Search
        self.directoryEntry = Entry(self.master)
        self.directoryEntry.grid(row=1,sticky=EW)

        self.directoryEntryButton = Button(self.master,text='Save', relief=SUNKEN)
        self.directoryEntryButton.grid(row=1,column=2,sticky=EW)

        self.Button = Button(self.master, text='Choose', command=self.dirFindEntry)
        self.Button.grid(row=1, column=1, sticky=EW)

        self.list = Listbox(self.master,yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.list.yview)
        self.scrollbar1.grid(row=2,column=1,rowspan=2,sticky=N+S+E+W)
        self.list.grid(row=2,rowspan=2,sticky=N+S+E+W)
        self.list.bind('<Double-Button-1>', self.OnDouble)
        self.list.bind('<Button-3>', self.createDir)

        # File Search
        self.directoryEntrySearch = Entry(self.master)
        self.directoryEntrySearch.grid(row=4, sticky=EW)

        self.directorySearchButton = Button(self.master, text='Insert', command=self.activate_search)
        self.directorySearchButton.grid(row=4, column=1, sticky=EW)

        self.search = Listbox(self.master, yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.search.yview)
        self.scrollbar2.grid(row=5, column=1, rowspan=2, sticky=N + S + E + W)
        self.search.grid(row=5, rowspan=2, sticky=N + S + E + W)
        self.search.bind('<Double-Button-1>', self.OnDouble)
        self.search.bind('<Button-3>', self.createDir)

        # Create Directory
        self.ModEntry = Entry(self.master)
        self.ModEntry.grid(row=7, sticky=EW)

        self.ModEntryButton = Button(self.master, text='Save', relief=SUNKEN)
        self.ModEntryButton.grid(row=7, column=2, sticky=EW)

        self.ButtonMod = Button(self.master, text='Choose', command=self.dirFindEntryMod)
        self.ButtonMod.grid(row=7, column=1, sticky=EW)

        self.listMod = Listbox(self.master, yscrollcommand=self.scrollbar1.set)
        self.scrollbar3.config(command=self.listMod.yview)
        self.scrollbar3.grid(row=8, column=1, rowspan=2, sticky=N + S + E + W)
        self.listMod.grid(row=8, rowspan=2, sticky=N + S + E + W)
        self.listMod.bind('<Double-Button-1>', self.OnDouble)



    def createDir(self,event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        value = value.replace(self.entry, "")
        file = value.split('\\')
        file = file[-1]
        value = value.replace('\\' + file, '')
        value = self.Mod + value
        os.makedirs(value, exist_ok=True)
        f = open(value + '\\' + file, mode='w' )
        f.close()
        self.saveEntryMod()



    def dirFindEntry(self):
        if self.directoryEntry != '':
            self.directoryEntry.delete(0, END)
        self.filename = filedialog.askdirectory(initialdir="/", title="Select file")
        self.directoryEntry.insert(0,self.filename)
        self.directoryEntryButton.grid_remove()
        self.directoryEntryButton = Button(self.master, text='Save', command=self.saveEntry)
        self.directoryEntryButton.grid(row=1, column=2, sticky=EW)

    def dirFindEntryMod(self):
        if self.ModEntry != '':
            self.ModEntry.delete(0, END)
        self.filename = filedialog.askdirectory(initialdir="/", title="Select file")
        self.ModEntry.insert(0,self.filename)
        self.ModEntryButton.grid_remove()
        self.ModEntryButton = Button(self.master, text='Save', command=self.saveEntryMod)
        self.ModEntryButton.grid(row=7, column=2, sticky=EW)

    def saveEntry(self):
        self.list.delete(0,END)
        self.entry = self.directoryEntry.get()
        lst = findDirectories(['.txt','.yml', '.lua'],self.entry)
        for item in lst:
            self.list.insert(END, item)

    def saveEntryMod(self):
        self.listMod.delete(0,END)
        self.Mod = self.ModEntry.get()
        lst = findDirectories(['.txt', '.yml', '.lua'], self.Mod)
        for item in lst:
            self.listMod.insert(END, item)

    def activate_search(self):
        self.search.delete(0,END)
        entry = self.directoryEntrySearch.get()
        self.directoryEntrySearch.delete(0, END)
        lst = search(['.txt','.yml', '.lua'], self.entry, entry)
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