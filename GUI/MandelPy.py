# MandelPy.py
# =============================================================================
#
# AUTHOR:           Franziska Schmidt (www.astrofranzi.com)
# CREATION DATE:    26.12.2018
# PROJECT:          Outreach
# DESCRIPTION:      Main driver for MandelPy
# NOTES:            -
# HISTORY:          26.12.2018: Source file creation (F.Schmidt)
# =============================================================================



# Import libraries ------------------------------------------------------------
import tkinter

# Import external scripts
from classWidget import Widget
# -----------------------------------------------------------------------------




# Main Driver
# -----------------------------------------------------------------------------

# Set up root widget
root = tkinter.Tk()

# Set title of Widget
root.title("MandelPy by F. Schmidt (www.astrofranzi.com)")

# Set size of widget
root.geometry('1400x700')


# Generate the Widget
widget = Widget(root)

# Start widget
root.mainloop()
