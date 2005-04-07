#!/usr/bin/env python

__version__ = "$Revision: 1.1.1.1 $"

from autolog import autolog
import unittest

autolog.error("error test")

if __name__ == "__main__":
    unittest.main()
