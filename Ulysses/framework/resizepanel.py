'''
Created on May 18, 2014

Usage:
 - Create the WindowLayout of the Window (footprints of each Panel) 
 - Create a Window with the WindowLayout
 - Create all Panel elements
   - Populate each Panel as desired
 - Add each Panel to a position in the Window

TODO:  Create fully resizable Window model with tk.PanedWindow
       Don't grid the PanedWindows, just add them.
       To support proper adding, when Window.addPanel, just add to index in list
       then on show, actually call add in order.  OR use .insert()
'''
from tkinter import ttk
import tkinter as tk
import copy


fillAll = (tk.N, tk.W, tk.E, tk.S)
fillEW = (tk.W, tk.E)
fillNS = (tk.N, tk.S)

class PanelSize(object):
    '''
    The details of the size of a Panel in grid terms
    '''
    
    def __str__(self):
        return"[(%d,%d) -%d |%d]" % (self.row, self.col, self.width, self.height)
    
    def __repr__(self):
        return"[(%d,%d) -%d |%d]" % (self.row, self.col, self.width, self.height)

    def __init__(self,
                 row: "Upper-left row start point" = 1,
                 col: "Upper-left column start point" = 1,
                 width = 1,
                 height = 1):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        
class Panel(object):
    '''
    A reusable component of a Window, a Panel is a section of the display
    '''
    
    def __init__(self,
                 relief: "flat, raised, sunken, solid, ridge, groove" = 'flat', 
                 parent: tk.Widget = None):
        '''
        @type parent: tk.Widget
        '''
        self.relief = relief
        self.parent = parent
        self.frame = self.__createFrame();
    
    def __createFrame(self) -> ttk.Frame:
        '''
        @rtype: ttk.Frame
        '''
        frame = ttk.Frame(self.parent)
        frame['padding'] = (5, 5)
        frame['borderwidth'] = 2
        frame['relief'] = self.relief
        return frame
    
class WindowLayout(object):
    '''
    The WindowLayout describes how the Panel elements are arranged
    No error handling here, so don't do dumb things (rectangles only)!
    '''
    
    def __str__(self):
        return str(self.panelSizes)
    
    def __repr__(self):
        return str(self.panelSizes)
    
    def __init__(self,
                 layout: "Each element describes a column of each row" =[]):
        '''
        @type layout: List
        '''
        self.__createByArray(layout)
    
    def __createByArray(self,
                        layout: "Each element describes a column of each row" =[]):
        '''
        Go through array of numbers describing indices of Window, wherein each
        array element is a row, and each number in the string is the index of
        the Panel element in the Window at that column.
        ["11", "23"] = Panel 1 on top row, 2 at bottom left, 3 at bottom right
        @type layout: List
        '''
        self.panelSizes = {}
        panelIndices = []
        self.rows = len(layout)
        self.columns = 0
        if self.rows > 0:
            self.columns = len(layout[0])
        for r, row in enumerate(layout):
            # Keep track so we don't add width to indices we've already seen
            colsForPanelsHandled = copy.deepcopy(panelIndices)
            heightForPanelsHandled = []
            for c, col in enumerate(row):
                index = int(col)
                if index not in colsForPanelsHandled:
                    self.__updatePanelWidth(index, r, c, panelIndices)
                elif index not in heightForPanelsHandled:
                    self.panelSizes[index].height += 1
                    heightForPanelsHandled.append(index)
    
    def __updatePanelWidth(self, index, r, c, panelIndices):
        if index not in self.panelSizes:
            self.panelSizes[index] = PanelSize(row=r, col=c)
        else:
            self.panelSizes[index].width += 1
        if index not in panelIndices:
            panelIndices.append(index)
    
class Window(ttk.Frame):
    '''
    A Window is composed of any number of Panel elements 
    '''
    def __init__(self,
                 layout: WindowLayout,
                 title = "Dynamic Window Title",
                 root = tk.Tk()):
        '''
        @type layout: WindowLayout
        @type parent: tk.
        '''
        self.root = root
        ttk.Frame.__init__(self, self.root)
        self.root.title(title)
        self.layout = layout
        
    def addPanel(self,
                 panel: Panel,
                 position: "Position at which to add panel"):
        '''
        Add a Panel to the Window at the desired position
        @type panel: Panel
        '''
        panelSize = self.layout.panelSizes[position]
        panel.frame.grid(column=panelSize.col,
                         row=panelSize.row,
                         columnspan=panelSize.width,
                         rowspan=panelSize.height,
                         sticky=fillAll)
    
    def show(self):
        '''
        Display the Window
        '''
        self.__applyUniformExpansion()
        self.mainloop()
    
    def __applyUniformExpansion(self):
        for r in range(self.layout.rows):
            self.root.rowconfigure(r, weight=1)
        for c in range(self.layout.columns):
            self.root.columnconfigure(c, weight=1)

if __name__ == "__main__":
    print("Running Simple Window Test")
    layout = WindowLayout(["11133",
                           "11133",
                           "11122",
                           "44422"]) 
    window = Window(layout)
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
