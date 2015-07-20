#!/usr/bin/python
# -*- coding: utf-8 -*-

# simple.py

import sys
from PySide import QtGui

from spreadsheet.window import SpreadsheetWindow

app = QtGui.QApplication(sys.argv)

# TODO: Create spreadsheet here
wid = SpreadsheetWindow()
wid.show()

sys.exit(app.exec_())
