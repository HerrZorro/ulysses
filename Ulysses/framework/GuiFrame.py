'''
Created on May 7, 2014

Operations:
 - Create a Window
 - Create the PanelLayout of the Window (footprints of each Panel) 
 - Create all Panel elements
   - Populate each Panel as desired
 - Tell the Window where the Panel should go
 - Have the Window grid each Panel based on the PanelLayout
'''
from tkinter import ttk
import tkinter as tk

class PanelSize(object):
    '''
    The details of the size of a Panel in grid terms
    '''

    def __init__(self,
                 width = 1,
                 height = 1):
        self.width = width
        self.height = height
        
class Panel(object):
    '''
    A reusable component of a Window, a Panel is a section of the display
    '''
    
    def __init__(self,
                 relief: "flat, raised, sunken, solid, ridge, groove" = 'flat', 
                 parent = None):
        self.relief = relief
        self.parent = parent
        self.frame = self.createFrame();
    
    def createFrame(self) -> ttk.Frame:
        frame = ttk.Frame(self.parent)
        frame['padding'] = (5, 5)
        frame['borderwidth'] = 2
        frame['relief'] = self.relief
        # TODO:  get better way to make Panel internal columns fill...
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        return frame
    
class Window(ttk.Frame):
    '''
    A Window is composed of any number of Panel elements 
    '''
    def __init__(self):
        self.root = tk.Tk()
        ttk.Frame.__init__(self, self.root)
        self.root.title("Dynamic Window")
        self.fill = (tk.N, tk.W, tk.E, tk.S)
        self.layout = {}
        
    def setLayout(self,
                  details: PanelSize,
                  position):
        self.layout[position] = details
        
    def addPanel(self,
                 panel: Panel,
                 position):
        # TODO:  implement where to add panel
        panel.frame.grid(column=position, row=0, sticky=self.fill)
    
    def show(self):
        # TODO:  Correct Window filling...
        index = 0
        print(self.layout)
        for position, panelSize in self.layout.items():
            self.root.columnconfigure(position, weight=1)
            index += 1
        self.mainloop()

window = Window()
window.setLayout(PanelSize(), 1)
window.setLayout(PanelSize(), 2)
p1 = Panel(relief='raised', parent=window.root)
ttk.Checkbutton(p1.frame,
                text='Use Phone',
                variable=tk.StringVar(),
                onvalue='yes',
                offvalue='no').grid()
p2 = Panel(relief='ridge', parent=window.root)
ttk.Radiobutton(p2.frame, text='Home', variable=tk.StringVar(),
                value='home').grid(sticky=tk.W)
ttk.Radiobutton(p2.frame, text='Office', variable=tk.StringVar(),
                value='office').grid(sticky=tk.W)
ttk.Radiobutton(p2.frame, text='Mobile', variable=tk.StringVar(),
                value='cell').grid(sticky=tk.W)
window.addPanel(p1, 1)
window.addPanel(p2, 2)
window.show()
