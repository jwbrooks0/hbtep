
""" 
import entire module and all sub-modules
also reloads modules and submodules
"""

import sys
if sys.version_info.major==3:
	osVer=3
	import importlib
else:
	osVer=2

# contains read/write/processcp  code relating to HBT.  This code loads the majority of the code from the Tree
import _getHBTData as get
if osVer==2:
	reload(get)
else:
	importlib.reload(get)

# misc. data processing functions
import _processData as process
if osVer==2:
	reload(process)
else:
	importlib.reload(process)

# plotting toolkit, second generation
import os # with X11 Protection
#if os.environ.has_key('DISPLAY'): # TODO not compatible with python3.  please fix.  I'm (John) disabling it for now.
import _plotTools as plot
if osVer==2:
	reload(plot)
else:
	importlib.reload(plot)

# misc plasma related code
import _processPlasma as processPlasma
if osVer==2:
	reload(processPlasma)
else:
	importlib.reload(processPlasma)

# misc data read/write tools
import _rwDataTools as readWrite
if osVer==2:
	reload(readWrite)
else:
	importlib.reload(readWrite)
    
# functions related to the caliban control computer
import _controlCaliban as control
if osVer==2:
	reload(control)
else:
	importlib.reload(control)
    

"""
how to reload modules.  This allows the all subpackages to be reloaded when 
the main package is reloaded.

# e.g.
import hbtepLib as hbt
# then after you make modification to _rwHBTDataTools.py, type:
reload(hbt)
# now, hbt and its subfunctions are up to date.  
"""

