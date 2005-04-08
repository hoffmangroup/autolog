#!/usr/bin/env python
from __future__ import division

__version__ = "$Revision: 1.2 $"

import inspect
import logging
import logging.config
from path import path
import sys

LOGGINGRC_PATH = path("~/.loggingrc").expand()

if LOGGINGRC_PATH.exists():
    logging.config.fileConfig(path(LOGGINGRC_PATH))
else:
    logging.basicConfig()

class AutoLog(object):
    def __getitem__(self, name):
        if name.startswith("."):
            name = self._defaultname() + name
            
        return logging.getLogger(name)

    def __getattr__(self, name):
        """
        call the default logger for anything other than item
        subscripting
        """
        return getattr(self[self._defaultname()], name)

    @staticmethod
    def _defaultname(stacklevel=2):
        res = inspect.stack()[stacklevel][0].f_globals["__name__"]
        
        if res == "__main__":
            res = path(sys.argv[0]).namebase

        if not res:
            res = "root"

        return res

autolog = AutoLog()
