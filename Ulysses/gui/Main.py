'''
Created on May 11, 2014
'''

from tkinter import ttk

from framework.GuiFrame import Panel
from framework.GuiFrame import Window
from framework.GuiFrame import WindowLayout
from framework.GuiFrame import fillAll
from framework.GuiFrame import fillEW
from framework.GuiFrame import fillNS
import tkinter as tk


class HUD(object):
    '''
    classdocs
    '''
    textWidth = 50

    def __init__(self):
        '''
        Constructor
        '''
        self.createWindow()
        self.createMenuBar()
        
        self.createMapPanel()
        self.createStoryPanel()
        self.createInputPanel()
        self.createStatusPanel()
        self.createInventoryPanel()
        self.createPartyPanel()
        
        self.window.show()
        
    def createWindow(self):
        self.layout = WindowLayout(["114",
                                    "114",
                                    "115",
                                    "115",
                                    "226",
                                    "226",
                                    "227",
                                    "337",])
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
        
    def createMapPanel(self):
        self.mapPanel = Panel(relief='ridge', parent=self.root)
        panel = self.mapPanel
        tk.Text(panel.frame,
                height=10,
                width=self.textWidth,
                state=tk.DISABLED).grid(sticky=fillAll)
        panel.frame.columnconfigure(0, weight=1)
        panel.frame.rowconfigure(0, weight=1)
        self.window.addPanel(panel, 1)
    
    def createStoryPanel(self):
        self.storyPanel = Panel(relief='ridge', parent=self.root)
        panel = self.storyPanel
        tk.Text(panel.frame,
                height=7,
                width=self.textWidth,
                state=tk.DISABLED).grid(sticky=fillAll)
        panel.frame.columnconfigure(0, weight=1)
        panel.frame.rowconfigure(0, weight=1)
        self.window.addPanel(panel, 2)
    
    def createInputPanel(self):
        self.inputPanel = Panel(relief='ridge', parent=self.root)
        panel = self.inputPanel
        tk.Text(panel.frame,
                height=1,
                width=self.textWidth).grid(column=0, columnspan=3, row=0,
                                           sticky=fillAll)
        tk.Button(panel.frame,
                  text="Enter").grid(column=3, row=0, sticky=fillAll)
        panel.frame.columnconfigure(0, weight=1)
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
        tk.Label(panel.frame, text="Inventory:").grid(sticky=(tk.N, tk.W))
        panel.frame.columnconfigure(0, weight=1)
        panel.frame.rowconfigure(0, weight=1)
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

if __name__ == "__main__":
    hud = HUD()