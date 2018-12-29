"""
scrimpy.py

A simple Python module to be used as a base for single file batch scripts.
Instead of creating `.bat` files on Windows, scrimpy can be used.
Never use this codebase for something larger than single file batch scripts.
"""

# pylint: disable=missing-docstring
# pylint: disable=C0111
# C0111 - Missing %s docstring
# C:  1, 0: Missing module docstring (missing-docstring)
# C: 13, 0: Missing function docstring (missing-docstring)

# pylint: disable=invalid-name
# pylint: disable=C0103
# C: 10, 0: Invalid constant name "variable1" (invalid-name)

# pylint: disable=line-too-long
# pylint: disable=C0301
# C: 22, 0: Line too long (127/100) (line-too-long)

# pylint: disable=trailing-newlines
# pylint: disable=C0303
# C: 59, 0: Trailing newlines (trailing-newlines)

# from __future__ import print_function

import os  # pylint: disable=unused-import
import shutil  # pylint: disable=unused-import
import sys  # pylint: disable=unused-import

# change directory to script dir
starting_dir = os.getcwd()
os.chdir(os.path.abspath(os.path.dirname(__file__)))

# type your code here.

print("scrimpy loaded and finished.")
os.chdir(starting_dir)
