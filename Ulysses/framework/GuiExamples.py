'''
Created on May 4, 2014
'''
from tkinter import ttk
from tkinter import PanedWindow
import random

import tkinter as tk


class GuiExamples(ttk.Frame):
    def __init__(self, master=None):
        master.title("GUI Examples")
        ttk.Frame.__init__(self, master)
        
        self.createMenuBar()
        self.createRightClickMenu()
        
        self.createFeetToMetersFrame()
        self.createEventsFrame()
        self.createTestFrame()
        self.createThemeFrame()
        self.createResizableFrame()
        self.createTabbedFrame()
        self.createForgottenFrame()
        self.createHelloWorldFrame()
        
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)
        
        
    def createMenuBar(self):
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New",
                             command=self.doNothing)
        filemenu.add_command(label="Open",
                             command=self.doNothing())
        filemenu.add_command(label="Save",
                             command=self.doNothing)
        filemenu.add_command(label="Save as...",
                             command=self.doNothing)
        filemenu.add_command(label="Close", command=self.doNothing)
        
        filemenu.add_separator()
        
        filemenu.add_command(label="Exit", command=self.master.quit)
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
        
        self.master.config(menu=menubar)
    
    def createRightClickMenu(self):
        rightClickMenu = tk.Menu(self.master, tearoff=0)
        for i in ('One', 'Two', 'Three'):
            rightClickMenu.add_command(label=i)
        if (root.tk.call('tk', 'windowingsystem')=='aqua'):
            root.bind('<2>', lambda e: rightClickMenu.post(e.x_root, e.y_root))
            root.bind('<Control-1>', lambda e: rightClickMenu.post(e.x_root, e.y_root))
        else:
            root.bind('<3>', lambda e: rightClickMenu.post(e.x_root, e.y_root))

    def createFeetToMetersFrame(self):
        self.feet = tk.StringVar()
        self.meters = tk.StringVar()
        
        self.f2mFrame = self.getFrame('sunken')
        self.f2mFrame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.f2mFrame.columnconfigure(0, weight=1)
        self.f2mFrame.rowconfigure(0, weight=1)
        
        feet_entry = ttk.Entry(self.f2mFrame, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        
        ttk.Label(self.f2mFrame,
                  textvariable=self.meters).grid(column=2,
                                                 row=2,
                                                 sticky=(tk.W, tk.E))
        ttk.Button(self.f2mFrame,
                   text="Calculate",
                   command=self.calculate).grid(column=2,
                                                row=3,
                                                columnspan=2,
                                                sticky=(tk.W, tk.E))
        
        ttk.Label(self.f2mFrame, text="feet").grid(column=3, row=1, sticky=tk.W)
        ttk.Label(self.f2mFrame,
                  text="is equivalent to").grid(column=1,
                                                row=2,
                                                sticky=tk.E)
        ttk.Label(self.f2mFrame, text="meters").grid(column=3,
                                                     row=2,
                                                     sticky=tk.W)
        
        for child in self.f2mFrame.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
        feet_entry.focus()
        self.master.bind('<Return>', self.calculate)
        
    def createEventsFrame(self):
        self.eventFrame = self.getFrame('raised')
        self.eventFrame.grid(column=1, row=1)
        
        self.eventFrame.label = ttk.Label(self.eventFrame, text="Starting...")
        self.eventFrame.label.grid(sticky=(tk.N, tk.E, tk.S, tk.W))
        self.eventFrame.label.bind('<Enter>',
                                   lambda e: self.eventFrame.label.configure(text='Moved mouse inside'))
        self.eventFrame.label.bind('<Leave>',
                                   lambda e: self.eventFrame.label.configure(text='Moved mouse outside'))
        self.eventFrame.label.bind('<1>',
                                   lambda e: self.eventFrame.label.configure(text='Clicked left mouse button'))
        self.eventFrame.label.bind('<Double-1>',
                                   lambda e: self.eventFrame.label.configure(text='Double clicked'))
        self.eventFrame.label.bind('<B3-Motion>',
                                   lambda e: self.eventFrame.label.configure(text='right button drag to %d,%d' % (e.x, e.y)))
        
    def createTestFrame(self):
        self.testFrame = self.getFrame('solid')
        self.testFrame.grid(column=1, row=0)
        measureSystem = tk.StringVar()
        self.testFrame.check = ttk.Checkbutton(self.testFrame,
                                               text='Use Phone', 
                                               command=self.doNothing,
                                               variable=measureSystem,
                                               onvalue='yes',
                                               offvalue='no')
        self.testFrame.check.grid()
        phone = tk.StringVar()
        ttk.Radiobutton(self.testFrame, text='Home', variable=phone,
                        value='home').grid(sticky=tk.W)
        ttk.Radiobutton(self.testFrame, text='Office', variable=phone,
                        value='office').grid(sticky=tk.W)
        ttk.Radiobutton(self.testFrame, text='Mobile', variable=phone,
                        value='cell').grid(sticky=tk.W)
        
    def createThemeFrame(self):
        self.style = ttk.Style()
        available_themes = self.style.theme_names()
        random_theme = random.choice(available_themes)
        self.style.theme_use(random_theme)
        
        self.themeFrame = self.getFrame('ridge')
        self.themeFrame.grid(column=0, row=1)
#         self.themeFrame.pack(expand=True, fill='both')
        
        self.theme = tk.StringVar()
        self.theme.set(random_theme)
        self.themeFrame.label = tk.Label(self.themeFrame, textvariable=self.theme)
        self.themeFrame.label.pack(padx=1, pady=1)
        
        # create a Combobox with themes to choose from
        self.combo = ttk.Combobox(self.themeFrame, values=available_themes)
        self.combo.pack(padx=32, pady=8)
        # make the Enter key change the style
        self.combo.bind('<Return>', self.changeStyle)
        # make a Button to change the style
        button = ttk.Button(self.themeFrame, text='OK')
        button['command'] = self.changeStyle
        button.pack(pady=8)
        
    def createResizableFrame(self):
        self.resizeFrame = self.getFrame('groove')
        
        fill = (tk.N, tk.E, tk.S, tk.W)
        p1 = tk.PanedWindow(self.resizeFrame, orient=tk.HORIZONTAL)
        p2 = tk.PanedWindow(p1, orient=tk.VERTICAL)
        p1.grid(sticky=fill)
        p2.grid(sticky=fill)
        # first pane, which would get widgets gridded into it:
        isLabelframe = False
        if isLabelframe:
            f1 = ttk.Labelframe(p2, text='P1', width=5, height=5)
            f2 = ttk.Labelframe(p2, text='P2', width=5, height=5) # second pane
            f3 = ttk.Labelframe(p1, text='P3', width=5, height=10) # third pane
        else:
            f1 = ttk.Frame(p2, width=5, height=5)
            f2 = ttk.Frame(p2, width=5, height=5) # second pane
            f3 = ttk.Frame(p1, width=5, height=10) # third pane
        ttk.Label(f1, text='L1').grid()
        ttk.Label(f2, text='L2').grid()
        ttk.Label(f3, text='L3').grid()
        p2.add(f1, stretch='always')
        p2.add(f2, stretch='always')
        p1.add(p2, stretch='always')
        p1.add(f3, stretch='always')
        
        self.resizeFrame.grid(column=2, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.resizeFrame.columnconfigure(0, weight=1)
        self.resizeFrame.rowconfigure(0, weight=1)

    def createTabbedFrame(self):
        self.tabbedFrame = self.getFrame('flat')
        
        n = ttk.Notebook(self.tabbedFrame)
        n.grid(sticky=(tk.N, tk.E, tk.S, tk.W))
        f1 = ttk.Frame(n); # first page, which would get widgets gridded into it
        f2 = ttk.Frame(n); # second page
        n.add(f1, text='One')
        n.add(f2, text='Two')
        
        self.tabbedFrame.grid(column=2, row=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.tabbedFrame.columnconfigure(0, weight=1)
        self.tabbedFrame.rowconfigure(0, weight=1)
    
    def createHelloWorldFrame(self):
        self.hellowWorldFrame = self.getFrame('flat')
        self.hellowWorldFrame.grid(column=1, row=2, columnspan=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.hellowWorldFrame.columnconfigure(0, weight=1)
        self.hellowWorldFrame.rowconfigure(0, weight=1)
        
        self.hi_there = tk.Button(self.hellowWorldFrame)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.sayHi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self.hellowWorldFrame, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")
        
    def createForgottenFrame(self):
        frame = self.getFrame('groove')
        
        ttk.Button(frame,
                   text='Frame not saved to self').grid(sticky=(tk.W, tk.E))
        
        frame.grid(column=0, row=2, sticky=(tk.N, tk.W, tk.E, tk.S))
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
    def getFrame(self, relief):
        """
        flat, raised, sunken, solid, ridge, groove
        """
        frame = ttk.Frame(self.master)
        frame['padding'] = (5, 5)
        frame['borderwidth'] = 2
        frame['relief'] = relief
        return frame

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass
    
    def changeStyle(self, event=None):
        """set the Style to the content of the Combobox"""
        content = self.combo.get()
        try:
            self.style.theme_use(content)
        except tk.TclError as err:
            tk.messagebox.showerror('Error', err)
        else:
            self.theme.set(content)
        
    def doNothing(self, *args):
        pass

    def sayHi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = GuiExamples(master=root)
app.mainloop()
