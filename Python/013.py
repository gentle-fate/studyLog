# -*-  coding : uft-8 -*-
#module
import imp
import classBar
classBar.foo()
c = classBar.bar()
c.grok()
#
imp.reload(classBar)
if __name__ == "__main__":
	import sys
	print(sys.argv[0])
#!!!!
# .pyc  .pyo
#compileall
#pass
import sys
#print sys.ps1
#print sys.ps2
print sys.path
#
print dir(sys)
print dir(classBar)
#import builtins
#dir(builtins)
# __all__
#from . import echo
#from .. import formats
#from ..filters import equalizer
#__path__



































