'''
Created on May 11, 2014
'''

from tkinter import ttk
import tkinter.scrolledtext
import tkinter as tk

from framework.panel import Panel
from framework.panel import Window
from framework.panel import WindowLayout
from framework.panel import fillAll
from framework.panel import fillEW
from framework.panel import fillNS

from framework.widgets import ScrollListbox
from framework.widgets import ScrollText

class HUD(object):
    '''
    The main Heads Up Display
    '''
    textWidth = 40

    def __init__(self):
        '''
        Constructor
        '''
        self.createWindow()
        self.createMenuBar()
        
        self.createEnvironmentPanel()
        self.createDescriptionPanel()
        self.createInputPanel()
        self.createStatusPanel()
        self.createInventoryPanel()
        self.createPartyPanel()
        
        self.root.bind('<Return>', self.handleInput)
        
        self.window.show()
        
    def createWindow(self):
        self.layout = WindowLayout(["114",
                                    "114",
                                    "114",
                                    "115",
                                    "115",
                                    "225",
                                    "226",
                                    "226",
                                    "336"])
        self.window = Window(self.layout,
                             title="Ulysses")
        self.root = self.window.root
    
    def createMenuBar(self):
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New",
                             command=self.doNothing)
        filemenu.add_command(label="Open",
                             command=self.doNothing)
        filemenu.add_command(label="Save",
                             command=self.doNothing)
        filemenu.add_command(label="Save as...",
                             command=self.doNothing)
        filemenu.add_command(label="Close", command=self.doNothing)
        
        filemenu.add_separator()
        
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.doNothing)
        
        editmenu.add_separator()
        
        editmenu.add_command(label="Cut", command=self.doNothing)
        editmenu.add_command(label="Copy", command=self.doNothing)
        editmenu.add_command(label="Paste", command=self.doNothing)
        editmenu.add_command(label="Delete", command=self.doNothing)
        editmenu.add_command(label="Select All", command=self.doNothing)
        
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.doNothing)
        helpmenu.add_command(label="About...", command=self.doNothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        self.root.config(menu=menubar)
        
    def createEnvironmentPanel(self):
        # TODO:  Create a TextMap class to use here that handles updating
        self.environmentPanel = Panel(relief='ridge', parent=self.root)
        panel = self.environmentPanel
        tk.Text(panel.frame,
                height=10,
                width=self.textWidth,
                state=tk.DISABLED).grid(sticky=fillAll)
        panel.frame.columnconfigure(0, weight=1)
        panel.frame.rowconfigure(0, weight=1)
        self.window.addPanel(panel, 1)
    
    def createDescriptionPanel(self):
        self.descriptionPanel = Panel(relief='ridge', parent=self.root)
        panel = self.descriptionPanel
#         ScrolledText = tk.scrolledtext.ScrolledText
#         self.description = ScrolledText(panel.frame,
#                                         height=6,
#                                         width=self.textWidth,
#                                         state=tk.DISABLED)
        self.description = ScrollText(0, 0, panel.frame,
                                      charwidth=self.textWidth, height=6,
                                      state=tk.DISABLED)
        self.description.grid(sticky=fillAll)
        self.description.configure(font=("Ariel", 9))
        self.description.bind("<1>",
                              lambda e: self.description.focus_set())
        panel.frame.columnconfigure(0, weight=1)
        panel.frame.rowconfigure(0, weight=1)
        self.window.addPanel(panel, 2)
    
    def createInputPanel(self):
        self.inputPanel = Panel(relief='ridge', parent=self.root)
        panel = self.inputPanel
        self.input = tk.StringVar()
        tk.Label(panel.frame,
                 text=">").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(panel.frame,
                  textvariable=self.input).grid(column=1, columnspan=3, row=0,
                                                sticky=fillAll)
        tk.Button(panel.frame,
                  command=self.handleInput,
                  text="Submit").grid(column=4, row=0, sticky=fillAll)
        panel.frame.columnconfigure(1, weight=1)
        panel.frame.columnconfigure(2, weight=1)
        panel.frame.columnconfigure(3, weight=1)
        panel.frame.rowconfigure(0, weight=1)
        self.window.addPanel(panel, 3)
        
    def createStatusPanel(self):
        self.statusPanel = Panel(relief='raised', parent=self.root)
        panel = self.statusPanel
        tk.Label(panel.frame, text="Status:").grid(sticky=(tk.N, tk.W))
        panel.frame.columnconfigure(0, weight=1)
        panel.frame.rowconfigure(0, weight=1)
        self.window.addPanel(panel, 4)
        
    def createInventoryPanel(self):
        self.inventoryPanel = Panel(relief='raised', parent=self.root)
        panel = self.inventoryPanel
        tk.Label(panel.frame, text="Inventory:").grid(row=0, sticky=(tk.N, tk.W))
        ScrollListbox(0, 1, panel.frame).grid(sticky=fillAll)
        panel.frame.columnconfigure(0, weight=1)
        panel.frame.rowconfigure(1, weight=1)
        self.window.addPanel(panel, 5)
    
    def createPartyPanel(self):
        self.partyPanel = Panel(relief='raised', parent=self.root)
        panel = self.partyPanel
        tk.Label(panel.frame, text="Party:").grid(sticky=(tk.N, tk.W))
        panel.frame.columnconfigure(0, weight=1)
        panel.frame.rowconfigure(0, weight=1)
        self.window.addPanel(panel, 6)
    
    def doNothing(self):
        pass
    
    def handleInput(self, *args):
        if self.input.get() != "":
            userInput = self.input.get()
            
            # TODO:  Implement real code, don't just transfer text
            self.description.configure(state=tk.NORMAL)
            self.description.insert(tk.END, userInput + "\n")
            self.description.configure(state=tk.DISABLED)
            
            self.input.set("")

if __name__ == "__main__":
    hud = HUD()