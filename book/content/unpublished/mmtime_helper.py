# Import a module with the same name from a different directory.

import importlib
import os
import sys

projpath = '~/_dev/live-2022'

sys.path.insert(0, os.path.abspath(projpath))

# Temporarily hijack __file__ to avoid adding names at module scope;
# __file__ will be overwritten again during the reload() call.
__file__ = {'sys': sys, 'importlib': importlib}

del importlib
del os
del sys

__file__['importlib'].reload(__file__['sys'].modules[__name__])
