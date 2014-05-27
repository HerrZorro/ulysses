'''
Created on May 16, 2014
'''
from tkinter import ttk
import tkinter as tk

FILL=(tk.N, tk.E, tk.S, tk.W)
RIGHT=(tk.N, tk.E, tk.S)

def getBaseFrame(parent,
                 relief: "flat, raised, sunken, solid, ridge, groove" = 'flat'):
    frame = ttk.Frame(parent)
    #frame['padding'] = (5, 5)
    #frame['borderwidth'] = 2
    #frame['relief'] = relief
    return frame

class ScrollText(tk.Text):
    '''A scrolling tk.Text with simplified features'''
    def __init__(self,
                 column,
                 row,
                 master = None,
                 columnspan = 1,
                 rowspan = 1,
                 charwidth = 20,
                 **kw):
        '''
        Creates and places a scrolling tk.Text in parent at specified location,
        and returns the tk.Text
        '''
        frame = getBaseFrame(master)
        tk.Text.__init__(self, frame, kw, width=charwidth)
        scroll = ttk.Scrollbar(frame)
        scroll.grid(column=1, row=0, sticky=RIGHT)
        scroll.config(command=self.yview)
        self.config(yscrollcommand=scroll.set)
        self.grid(column=0, row=0, sticky=FILL)
        frame.grid(column=column, row=row,
                   rowspan=rowspan, columnspan=columnspan, sticky=FILL)
        frame.columnconfigure(index=0, weight=1)
        frame.rowconfigure(index=0, weight=1)
    
    def append(self, content):
        self.insert(tk.END, content)
    
    def appendAll(self,
                  values: list):
        '''
        @type values: list
        '''
        for value in values:
            self.insert(tk.END, value)
            
    def clear(self):
        self.delete("0.0", tk.END);

class ScrollListbox(tk.Listbox):
    '''A scrolling tk.Listbox with simplified features'''
    def __init__(self,
                 column,
                 row,
                 master = None,
                 columnspan = 1,
                 rowspan = 1,
                 charwidth = 20,
                 handler=None):
        '''
        Creates and places a scrolling tk.Listbox in parent at specified location,
        and returns the tk.Listbox
        '''
        frame = getBaseFrame(master)
        tk.Listbox.__init__(self, frame, width=charwidth)
        scroll = ttk.Scrollbar(frame)
        scroll.grid(column=1, row=0, sticky=RIGHT)
        scroll.config(command=self.yview)
        if handler:
            self.bind("<<ListboxSelect>>", handler)
        self.config(yscrollcommand=scroll.set)
        self.grid(column=0, row=0, sticky=FILL)
        frame.grid(column=column, row=row,
                   rowspan=rowspan, columnspan=columnspan, sticky=FILL)
        frame.columnconfigure(index=0, weight=1)
        frame.rowconfigure(index=0, weight=1)
    
    def append(self, value):
        self.insert(tk.END, value)
    
    def appendAll(self,
                  values: list):
        '''
        @type values: list
        '''
        for value in values:
            self.insert(tk.END, value)
            
    def clear(self):
        self.delete(0, tk.END);
    
