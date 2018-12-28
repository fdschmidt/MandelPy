# classWidget.py
# =============================================================================
#
# AUTHOR:           Franziska Schmidt (www.astrofranzi.com)
# CREATION DATE:    26.12.2018
# PROJECT:          Outreach
# DESCRIPTION:      Definition of the Widget class
#                   a Mandelbrot Set
# NOTES:            -
# HISTORY:          26.12.2018: Source file creation (F.Schmidt)
# =============================================================================


# Import libraries ------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import numpy as np
import tkinter
import tkinter.messagebox

# Import from external scripts
from fctMandelbrotSet import CalculateMandelbrotSet
from varGlobal import *

# -----------------------------------------------------------------------------





# Classes ---------------------------------------------------------------------

# Widget (class)
# =============================================================================
# Description: Widget
# Input:       -
# Output:      -
# History:     26.12.2018: Function created (F.Schmidt)
# =============================================================================

class Widget:
    def __init__(self, root):
        
        # Set frames and expand rule for input frame and plot frame
        frame1 = tkinter.Frame(root, width=400, height=700, 
                               background=bgColour)
        frame1.pack(padx=10, pady=10,side="left", fill="both", expand=True)
        frame2 = tkinter.Frame(root, width=1000, height=700, 
                               background=bgColour)
        frame2.pack(padx=10, pady=10,side="right", fill="both", expand=True)
        
        
        
        # Input Environment 
        # ---------------------------------------------------------------------
        
        # Add an empty row for a nicer layout
        labelPlaceholder = tkinter.Label(frame1, text="", background=bgColour)
        labelPlaceholder.grid(column=0, row=0)
        
        # Set header for input field
        text1 = tkinter.Label(frame1, text="   Parameters:", 
                              background=bgColour, font='Helvetica 14 bold')
        
        # Set position of header
        text1.grid(column=0, row=1)
        
        # Add an empty row for a nicer layout
        labelPlaceholder = tkinter.Label(frame1, text="", background=bgColour)
        labelPlaceholder.grid(column=0, row=2)
        
        
        # Set labels for input boxes
        labelXmin = tkinter.Label(frame1, text="xMin", background=bgColour)
        labelXmax = tkinter.Label(frame1, text="xMax", background=bgColour)
        
        labelYmin = tkinter.Label(frame1, text="yMin", background=bgColour)
        labelYmax = tkinter.Label(frame1, text="yMax", background=bgColour)
        
        labelXcells = tkinter.Label(frame1, text="xCells", background=bgColour)
        labelYcells = tkinter.Label(frame1, text="yCells", background=bgColour)
        
        labelItMaxs = tkinter.Label(frame1, text="Iterations", 
                                    background=bgColour)
        labelThreshold = tkinter.Label(frame1, text="Threshold", 
                                       background=bgColour)
        
        labelColourmap = tkinter.Label(frame1, text="Colourmap", 
                                       background=bgColour)
        
        
        # Set positions of input box labels
        labelXmin.grid(column=0, row=3)
        labelXmax.grid(column=0, row=4)
        
        labelYmin.grid(column=0, row=5)
        labelYmax.grid(column=0, row=6)
        
        labelXcells.grid(column=0, row=7)
        labelYcells.grid(column=0, row=8)
        
        labelItMaxs.grid(column=0, row=9)
        labelThreshold.grid(column=0, row=10)
        
        labelColourmap.grid(column=0, row=11)
        
        
        # Set string variable IDs for boxes
        self.xMinInput = tkinter.StringVar()
        self.xMaxInput = tkinter.StringVar()
        
        self.yMinInput = tkinter.StringVar()
        self.yMaxInput = tkinter.StringVar()
        
        self.xCellsInput = tkinter.StringVar()
        self.yCellsInput = tkinter.StringVar()
        
        self.itMaxInput = tkinter.StringVar()
        self.thresholdInput = tkinter.StringVar()
        
        self.colourMapInput = tkinter.StringVar()
        
        
        
        # Set input boxes
        boxXmin = tkinter.Entry(frame1,width=10,justify='right', 
                                textvariable=self.xMinInput)
        boxXmax = tkinter.Entry(frame1,width=10,justify='right', 
                                textvariable=self.xMaxInput)
        
        boxYmin = tkinter.Entry(frame1,width=10,justify='right', 
                                textvariable=self.yMinInput)
        boxYmax = tkinter.Entry(frame1,width=10,justify='right', 
                                textvariable=self.yMaxInput)
        
        boxXcells = tkinter.Entry(frame1,width=10,justify='right', 
                                  textvariable=self.xCellsInput)
        boxYcells = tkinter.Entry(frame1,width=10,justify='right', 
                                  textvariable=self.yCellsInput)
        
        boxItMax = tkinter.Entry(frame1,width=10,justify='right', 
                                 textvariable=self.itMaxInput)
        boxThreshold = tkinter.Entry(frame1,width=10,justify='right', 
                                     textvariable=self.thresholdInput)
        
        boxColourMap = tkinter.Entry(frame1,width=10,justify='right', 
                                     textvariable=self.colourMapInput)
        
        
        
        # Set default value in input box
        boxXmin.insert(0, str(xMin))
        boxXmax.insert(0, str(xMax))
        
        boxYmin.insert(0, str(yMin))
        boxYmax.insert(0, str(yMax))
        
        boxXcells.insert(0, str(xCells))
        boxYcells.insert(0, str(yCells))
        
        boxItMax.insert(0, str(itMax))
        boxThreshold.insert(0, str(threshold))
        
        boxColourMap.insert(0, colourMap)
        
        
        # Set backup values
        self.xMinOld = xMin
        self.xMaxOld = xMax
        self.yMinOld = yMin
        self.yMaxOld = yMax
        self.xCellsOld = xCells
        self.yCellsOld = yCells
        self.itMaxOld = itMax
        self.thresholdOld = threshold 

        
        
        # Set positions of input boxes
        boxXmin.grid(column=1, row=3)
        boxXmax.grid(column=1, row=4)
        
        boxYmin.grid(column=1, row=5)
        boxYmax.grid(column=1, row=6)
        
        boxXcells.grid(column=1, row=7)
        boxYcells.grid(column=1, row=8)
        
        boxItMax.grid(column=1, row=9)
        boxThreshold.grid(column=1, row=10)
        
        boxColourMap.grid(column=1, row=11)
        
        # Set string variable IDs for boxes
        self.checkSave = tkinter.IntVar()
        
        # Add a checkbox to give user the option to save the image
        tkinter.Checkbutton(frame1, text="Save image", variable=self.checkSave,
                            background=bgColour, activebackground=bgColour,
                            state="normal", offvalue=0, 
                            onvalue=1).grid(column=1, row=12, sticky="w")
        
        # ---------------------------------------------------------------------
        
        
        
        # Button
        # ---------------------------------------------------------------------
        
        # Add an empty row for a nicer layout
        labelPlaceholder = tkinter.Label(frame1, text="", background=bgColour)
        labelPlaceholder.grid(column=0, row=13)
        
        # Add button to re-calculate the Mandelbrot set 
        self.btn_CalcMandelbrot = tkinter.Button(frame1, 
                                    text="Calculate new Mandelbrot Set", 
                                    command=self.ButtonClicked)
        
        # Set position of the button
        self.btn_CalcMandelbrot.grid(column=1, row=14)
            
        # ---------------------------------------------------------------------
        
        
        
        # Calculate Mandelbrot Set for the Initial Plot
        # ---------------------------------------------------------------------
        
        # Generate grid for the Mandelbrot set
        xDomain = np.linspace(xMin, xMax, xCells)
        yDomain = np.linspace(yMin, yMax, yCells)
    
        # Generate empty Mandelbrot Set
        mandelbrot = np.zeros([yCells, xCells])
    
        # Calculate Mandelbrot Set
        mandelbrot = CalculateMandelbrotSet(xDomain, yDomain, mandelbrot, 
                                            threshold, itMax)
        
        # Generate backup data set
        self.mandelbrotBackup = mandelbrot
        
        # ---------------------------------------------------------------------
            
        
        
        # Generate Initial Plot in frame2
        # ---------------------------------------------------------------------
            
        # Initialise figure
        fig = plt.figure(figsize=(10, 10), dpi=100)
        pl = fig.add_subplot(111)
        fig.patch.set_facecolor(bgColour)
        
                    
        # Axis limits
        pl.set_xlim(xMin, xMax)
        pl.set_ylim(yMin, yMax)
        
        # Set font size of ticks
        for tick in pl.xaxis.get_major_ticks():
            tick.label.set_fontsize(10) 
        for tick in pl.yaxis.get_major_ticks():
            tick.label.set_fontsize(10) 
                
        # Labels
        pl.set_xlabel(r"Re",fontsize=12)
        pl.set_ylabel(r"Im",fontsize=12)
                
        # Colour boundaries
        bounds = np.linspace(0, 100, 300)
        norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
                
        # Colormesh plot
        pl.pcolormesh(xDomain, yDomain, mandelbrot[:,:], 
                             norm=norm, cmap=colourMap)
                
        # Equalize x and y axis
        plt.gca().set_aspect('equal', adjustable='box')
        
        # Set canvas for plot in frame 2
        self.canvas = FigureCanvasTkAgg(fig, master=frame2)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        frame2.pack()
        
        # ---------------------------------------------------------------------
        


    # ButtonClicked (member function)
    # =========================================================================
    # Description: Sets routines which will be carried out if button is clicked
    # Input:       -
    # Output:      -
    # History:     26.12.2018: Function created (F.Schmidt)
    # =========================================================================
    def ButtonClicked(self):
        
        # Check for invalid input
        lCheck = self.checkInput()    
        
        # Check whether new Mandelbrot Set needs to be calculated
        lRecalc = self.checkRecalc()
        
        # Obtain value from input boxes
        xMin = float(self.xMinInput.get())
        xMax = float(self.xMaxInput.get())
        yMin = float(self.yMinInput.get())
        yMax = float(self.yMaxInput.get())
        xCells = int(self.xCellsInput.get())
        yCells = int(self.yCellsInput.get())
        itMax = int(self.itMaxInput.get())
        threshold = float(self.thresholdInput.get())
        colourMap = self.colourMapInput.get()      
        lSave = int(self.checkSave.get())
        
        # Update Backup values for input
        self.xMinOld = xMin
        self.xMaxOld = xMax
        self.yMinOld = yMin
        self.yMaxOld = yMax
        self.xCellsOld = xCells
        self.yCellsOld = yCells
        self.itMaxOld = itMax
        self.thresholdOld = threshold 
        
        # Generate new grid for the Mandelbrot set
        xDomain = np.linspace(xMin, xMax, xCells)
        yDomain = np.linspace(yMin, yMax, yCells)
        
        
        # Values have changed and Mandelbrot set needs to be recalculated
        if (lRecalc and lCheck):
           
            # Generate new grid for the Mandelbrot set
            xDomain = np.linspace(xMin, xMax, xCells)
            yDomain = np.linspace(yMin, yMax, yCells)
            
            # Generate new empty Mandelbrot Set
            mandelbrot = np.zeros([yCells, xCells])
            
            # Calculate new Mandelbrot Set
            mandelbrot = CalculateMandelbrotSet(xDomain, yDomain, mandelbrot, 
                                                threshold, itMax)
            
            # Update backup data set
            self.mandelbrotBackup = mandelbrot
            
            
            
            # Display message depending on whether image will be saved or not
            if (lSave == 0):
                tkinter.messagebox.showinfo('Success', 
                                'New Mandelbrot Set has been calculated and' +
                                ' will now be plotted.')   
            else:
                tkinter.messagebox.showinfo('Success', 
                                'New Mandelbrot Set has been calculated ' + 
                                'and will now be plotted and saved.')             
            
            # Refresh figure
            self.RefreshFigure(xDomain, yDomain, xMin, xMax, yMin, yMax,
                                   colourMap, mandelbrot, lSave)
            
        # Values have not changed and plot just needs to be refreshed
        elif (lCheck):
            
            
            # Display message depending on whether image will be saved or not
            if (lSave == 0):
                tkinter.messagebox.showinfo('Success', 
                                'Mandelbrot Set will now be plotted.')   
            else:
                tkinter.messagebox.showinfo('Success', 
                                'Mandelbrot Set will now be plotted and saved.') 
            # Refresh figure
            self.RefreshFigure(xDomain, yDomain, xMin, xMax, yMin, yMax,
                                      colourMap, self.mandelbrotBackup, lSave)      
            
        
        
        
    # RefreshFigure (member function)
    # =========================================================================
    # Description: Refresh figure
    # Input:       -
    # Output:      -
    # History:     26.12.2018: Function created (F.Schmidt)
    # =========================================================================
    def RefreshFigure(self, xDomain, yDomain, xMin, xMax, yMin, yMax,
                               colourMap, mandelbrot, lSave):
            
        # Get parent canvas to draw on
        pl = self.canvas.figure.axes[0]
        
        # Set new axis limits of the plot
        pl.set_xlim(xMin, xMax)
        pl.set_ylim(yMin, yMax)
                
        # set new Colour boundaries
        bounds = np.linspace(0, 100, 300)
        norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
                
        # Generate new Colormesh plot
        pl.pcolormesh(xDomain, yDomain, mandelbrot[:,:], norm=norm, 
                             cmap=colourMap)
                
        # Equalize x and y axis
        plt.gca().set_aspect('equal', adjustable='box')
        
        # Update parent canvas
        self.canvas.draw()
        
        # Save Plot
        if (lSave == 1):
            
            # Initialise figure
            fig = plt.figure(figsize=(10, 10), dpi=dpiValue)
            pl = fig.add_subplot(111)
            fig.patch.set_facecolor(bgColour)
        
                    
            # Axis limits
            pl.set_xlim(xMin, xMax)
            pl.set_ylim(yMin, yMax)
        
            # Set font size of ticks
            for tick in pl.xaxis.get_major_ticks():
                tick.label.set_fontsize(16) 
            for tick in pl.yaxis.get_major_ticks():
                tick.label.set_fontsize(16) 
                
            # Labels
            pl.set_xlabel(r"Re",fontsize=18)
            pl.set_ylabel(r"Im",fontsize=18)
                
            # Colour boundaries
            bounds = np.linspace(0, 100, 300)
            norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
                
            # Colormesh plot
            pl.pcolormesh(xDomain, yDomain, mandelbrot[:,:], 
                             norm=norm, cmap=colourMap)
                
            # Equalize x and y axis
            plt.gca().set_aspect('equal', adjustable='box')
    
            
            # Determine name of the file
            filename = "MandelPy_{0}.png".format(datetime.now().strftime("%Y%m%d-%Hh%Mmin%Ss"))
            
            # Save image
            fig.savefig(filename)
            



    # checkInput (member function)
    # =========================================================================
    # Description: Checks whether all input values are valid
    # Input:       -
    # Output:      lCheck
    # History:     27.12.2018: Function created (F.Schmidt)
    # =========================================================================                   
    def checkInput(self):  
        
        # Initialize Boolean
        bol = True
  
        # Check whether the xMin entry is valid
        try:
            xMinTMP = float(self.xMinInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid xMin value.')    
            
        # Check whether the xMax entry is valid
        try:
            xMaxTMP = float(self.xMaxInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid xMax value.')  
            
        # Check whether the yMin entry is valid
        try:
            yMinTMP = float(self.yMinInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid yMin value.')  
            
        # Check whether the yMax entry is valid
        try:
            yMaxTMP = float(self.yMaxInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid yMax value.') 
            
        # Check whether the xCells entry is valid
        try:
            xCellsTMP = int(self.xCellsInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid xCell value.') 
        else:
            try:
                if (xCellsTMP <= 0):
                    raise ValueError
            except:
                bol = False
                tkinter.messagebox.showinfo('Error', 
                            'Invalid xCell value.')         
                
        # Check whether the yCells entry is valid
        try:
            yCellsTMP = int(self.yCellsInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid yCell value.') 
        else:
            try:
                if (yCellsTMP <= 0):
                    raise ValueError
            except:
                bol = False
                tkinter.messagebox.showinfo('Error', 
                            'Invalid yCell value.')     
                
        # Check whether the itMax entry is valid
        try:
            itMaxTMP = int(self.itMaxInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid Iterations value.') 
        else:
            try:
                if (itMaxTMP <= 0):
                    raise ValueError
            except:
                bol = False
                tkinter.messagebox.showinfo('Error', 
                            'Invalid Iterations value.') 
                
        # Check whether the threshold entry is valid
        try:
            thresholdTMP = float(self.thresholdInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid threshold value.') 
        else:
            try:
                if (thresholdTMP <= 0):
                    raise ValueError
            except:
                bol = False
                tkinter.messagebox.showinfo('Error', 
                            'Invalid threshold value.') 

        # Define list of all valid colour maps
        validColorMaps = ['viridis', 'plasma', 'inferno', 'magma','Greys', 
                          'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                          'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                          'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
                          'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 
                          'pink', 'spring', 'summer', 'autumn', 'winter',
                          'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 
                          'copper', 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 
                          'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 
                          'bwr', 'seismic', 'Pastel1', 'Pastel2', 'Paired', 
                          'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 
                          'tab20', 'tab20b', 'tab20c', 'flag', 'prism', 
                          'ocean', 'gist_earth', 'terrain', 'gist_stern',
                          'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 
                          'hsv', 'gist_rainbow', 'rainbow', 'jet', 
                          'nipy_spectral', 'gist_ncar']      

        # Check if colour map is valid
        try:
            colourMapTMP = str(self.colourMapInput.get())
        except:
            bol = False
            tkinter.messagebox.showinfo('Error', 
                            'Invalid colourmap value.\n' +
                            'All valid maps can be found here: ' +
                            'https://matplotlib.org/users/colormaps.html') 
        else:
            try:
                if (not (colourMapTMP in validColorMaps)):
                    raise ValueError
            except:
                bol = False
                tkinter.messagebox.showinfo('Error', 
                            'Invalid colour Map value.\n' +
                            'All valid maps can be found here: ' +
                            'https://matplotlib.org/users/colormaps.html')    
                
                
        return bol
                
                
    # checkRecalc (member function)
    # =========================================================================
    # Description: Checks whether a recalculation of the Mandelbrot set is
    #              necessary
    # Input:       -
    # Output:      Boolean
    # History:     27.12.2018: Function created (F.Schmidt)
    # =========================================================================                   
    def checkRecalc(self):  
        
        # Initialize return bollean
        bol = False
        
        # Get new entry values for inpuit parameters
        xMinNew = float(self.xMinInput.get())
        xMaxNew = float(self.xMaxInput.get())
        yMinNew = float(self.yMinInput.get())
        yMaxNew = float(self.yMaxInput.get())
        xCellsNew = int(self.xCellsInput.get())
        yCellsNew = int(self.yCellsInput.get())
        itMaxNew = int(self.itMaxInput.get())
        thresholdNew = float(self.thresholdInput.get())
        
        # Check whether entries have changed
        if (self.xMinOld != xMinNew):
            bol = True
        elif (self.xMaxOld != xMaxNew):
            bol = True
        elif (self.yMinOld != yMinNew):
            bol = True
        elif (self.yMaxOld != yMaxNew):
            bol = True
        elif (self.xCellsOld != xCellsNew):
            bol = True
        elif (self.yCellsOld != yCellsNew):
            bol = True   
        elif (self.itMaxOld != itMaxNew):
            bol = True
        elif (self.thresholdOld != thresholdNew):
            bol = True
        
        return bol
            
            
  
# -----------------------------------------------------------------------------