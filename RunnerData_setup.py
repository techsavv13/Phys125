
# ======================================================== #
# File automagically generated by GUI2Exe version 0.5.3
# Copyright: (c) 2007-2012 Andrea Gavana
# ======================================================== #

# Let's start with some default (for me) imports...
#nah sis, ima do my own thing
from cx_Freeze import setup, Executable
import sys,os

#sys.path.append('C:/Compiled/Phys125')
sys.argv.append("build")

dest = '/Users/Savvie/Phys125/Phys125'
# Process the includes, excludes and packages first

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
path = []

# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.

# No custom code added



GUI2Exe_Target_1 = Executable(
    # what to build
    script = "OrbitsimVPY.py",
    #initScript = None,
    base = 'Win32GUI',
    #targetName = "orbitSimVPY.exe",
    icon = None
    )
'''
GUI2Exe_Target_2 = Executable(
    # what to build
    script = "RunnerDataEnter.py",
    initScript = None,
    base = 'Win32GUI',
    targetName = "RunnerDataEnter.exe",
    icon = None
    )

GUI2Exe_Target_3 = Executable(
    # what to build
    script = "RunnerDataXmtSpot.py",
    initScript = None,
    base = 'Win32GUI',
    targetName = "RunnerDataXmtSpot.exe",
    icon = None
    )

GUI2Exe_Target_4 = Executable(
    # what to build
    script = "RunnerDataSimulator.py",
    initScript = None,
    base = 'Win32GUI',
    targetName = "RunnerDataSimulator.exe",
    icon = None
    )

'''
# That's serious now: we have all (or almost all) the options cx_Freeze
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.

setup(
    
    version = "0.1",
    description = "No Description",
    author = "savvie",
    name = "cx_Freeze Sample File",
    
    options = {"build_exe": {"includes": includes,
                             "excludes": excludes,
                             "packages": packages,
                             "path": path,
                             'build_exe' : r"C:\Compiled\Phys125"
                             }
               },
                           
    executables = [GUI2Exe_Target_1]
    )

# This is a place where any post-compile code may go.
# You can add as much code as you want, which can be used, for example,
# to clean up your folders or to do some particular post-compilation
# actions.

# No post-compilation code added


# And we are done. That's a setup script :-D

