from tkinter import filedialog
from tkinter import *
from Search import *


class UI:
    def __init__(self, master):
        # Window Size
        self.master = master
        self.master.wm_title('Hopefully Stellaris Modding API')
        self.master.minsize(width=1080, height=640)
        self.master.maxsize(width=1080, height=640)
        self.master.grid_columnconfigure(0, weight=1)
        menubar = Menu(self.master)

        # Menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Help", command=start_menu)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

        # ScrollBars
        self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)

        self.scrollbar2 = Scrollbar(self.master, orient=VERTICAL)

        self.scrollbar3 = Scrollbar(self.master, orient=VERTICAL)

        # Labels
        self.directoryLabel = Label(self.master, text='Insert Stellaris folder directory')
        self.directoryLabel.grid(row=0, sticky=EW)

        self.searchLabel = Label(self.master, text='Search something from Stellaris folder')
        self.searchLabel.grid(row=4, sticky=EW)

        self.modLabel = Label(self.master, text='Insert Stellaris Mod directory')
        self.modLabel.grid(row=8, sticky=EW)

        # Directory Search
        self.directoryEntry = Entry(self.master)
        self.directoryEntry.grid(row=1, sticky=EW)

        self.directoryEntryButton = Button(self.master, text='Save', relief=SUNKEN, fg='grey')
        self.directoryEntryButton.grid(row=1, column=2, sticky=EW)

        self.Button = Button(self.master, text='Choose', command=self.dir_find_entry)
        self.Button.grid(row=1, column=1, sticky=EW)

        self.list = Listbox(self.master, yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.list.yview)
        self.scrollbar1.grid(row=2, column=1, rowspan=2, sticky=N + S + E + W)
        self.list.grid(row=2, rowspan=2, sticky=N + S + E + W)
        self.list.bind('<Double-Button-1>', self.on_double)
        self.list.bind('<Button-3>', self.create_dir)

        # File Search
        self.directoryEntrySearch = Entry(self.master)
        self.directoryEntrySearch.grid(row=5, sticky=EW)

        self.directorySearchButton = Button(self.master, text='Search', relief=SUNKEN, fg='grey')
        self.directorySearchButton.grid(row=5, column=1, sticky=EW)

        self.search = Listbox(self.master, yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.config(command=self.search.yview)
        self.scrollbar2.grid(row=6, column=1, rowspan=2, sticky=N + S + E + W)
        self.search.grid(row=6, rowspan=2, sticky=N + S + E + W)
        self.search.bind('<Double-Button-1>', self.on_double)
        self.search.bind('<Button-3>', self.create_dir)

        # Create Directory
        self.ModEntry = Entry(self.master)
        self.ModEntry.grid(row=9, sticky=EW)

        self.ModEntryButton = Button(self.master, text='Save', relief=SUNKEN, fg='grey')
        self.ModEntryButton.grid(row=9, column=2, sticky=EW)

        self.ButtonMod = Button(self.master, text='Choose', command=self.dir_find_entry_mod)
        self.ButtonMod.grid(row=9, column=1, sticky=EW)

        self.listMod = Listbox(self.master, yscrollcommand=self.scrollbar1.set)
        self.scrollbar3.config(command=self.listMod.yview)
        self.scrollbar3.grid(row=10, column=1, rowspan=2, sticky=N + S + E + W)
        self.listMod.grid(row=10, rowspan=2, sticky=N + S + E + W)
        self.listMod.bind('<Double-Button-1>', self.on_double)

    # Make directory with file
    def create_dir(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        value = value.replace(self.entry, "")
        file = value.split('\\')
        file = file[-1]
        value = value.replace('\\' + file, '')
        value = self.Mod + value
        os.makedirs(value, exist_ok=True)
        f = open(value + '\\' + file, mode='w')
        f.close()
        self.save_entry_mod()

    # Get Text for Directory Entry
    def dir_find_entry(self):
        if self.directoryEntry != '':
            self.directoryEntry.delete(0, END)
        self.filename = filedialog.askdirectory(initialdir="/", title="Select file")
        self.directoryEntry.insert(0, self.filename)
        self.directoryEntryButton.grid_remove()
        self.directoryEntryButton = Button(self.master, text='Save', command=self.save_entry)
        self.directoryEntryButton.grid(row=1, column=2, sticky=EW)

    # Get Text fir Mod Directory Entry
    def dir_find_entry_mod(self):
        if self.ModEntry != '':
            self.ModEntry.delete(0, END)
        self.filename = filedialog.askdirectory(initialdir="/", title="Select file")
        self.ModEntry.insert(0, self.filename)
        self.ModEntryButton.grid_remove()
        self.ModEntryButton = Button(self.master, text='Save', command=self.save_entry_mod)
        self.ModEntryButton.grid(row=9, column=2, sticky=EW)

    # Save Text for Directory Entry
    def save_entry(self):
        self.list.delete(0, END)
        self.entry = self.directoryEntry.get()
        self.directorySearchButton.grid_remove()
        self.directorySearchButton = Button(self.master, text='Search', command=self.activate_search)
        self.directorySearchButton.grid(row=5, column=1, sticky=EW)
        lst = findDirectories(['.txt', '.yml', '.lua'], self.entry)
        for item in lst:
            self.list.insert(END, item)

    # Save Text for Mod Directory Entry
    def save_entry_mod(self):
        self.listMod.delete(0, END)
        self.Mod = self.ModEntry.get()
        os.chmod(self.Mod, 0o644)
        lst = findDirectories(['.txt', '.yml', '.lua'], self.Mod)
        for item in lst:
            self.listMod.insert(END, item)

    def activate_search(self):
        self.search.delete(0, END)
        entry = self.directoryEntrySearch.get()
        self.directoryEntrySearch.delete(0, END)
        lst = search(['.txt', '.yml', '.lua'], self.entry, entry)
        for item in lst:
            self.search.insert(END, item)

    def on_double(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        openFile(value)


class HelpMenu:
    def __init__(self, master):
        # Window Size
        self.master = master

        self.label = Label(self.master, text=""" Controls:
        --------------------------------------------------
        Opening file -- Double-Click on the directory to open file
        Creating empty file -- Choose with left click the file you wish to copy and then right click on to create empty file.""")
        self.label.pack(side=LEFT)


def start_menu():
    root = Tk()
    start = HelpMenu(root)
    root.mainloop()


def start():
    root = Tk()
    start = UI(root)
    root.mainloop()
