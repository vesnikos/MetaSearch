# -*- coding: utf-8 -*-
###############################################################################
#
# CSW Client
# ---------------------------------------------------------
# QGIS Catalogue Service client.
#
# Copyright (C) 2010 NextGIS (http://nextgis.org),
#                    Alexander Bruy (alexander.bruy@gmail.com),
#                    Maxim Dubinin (sim@gis-lab.info)
#
# Copyright (C) 2014 Tom Kralidis (tomkralidis@gmail.com)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
###############################################################################

import webbrowser

from PyQt4.QtGui import QDialog

from MetaSearch.util import get_ui_class

BASE_CLASS = get_ui_class('recorddialog2.ui')


class RecordDialog2(QDialog, BASE_CLASS):
    """Record Metadata Dialogue"""
    def __init__(self, record):
        """
        :param record: <class 'owslib.csw.CswRecord'>
        """

        QDialog.__init__(self)
        self.setupUi(self)
        self.path = None

        self.pteText.setPlainText(record.abstract)
        self.leTitle.setText(str(type(record)))
        self.tbOpenLocation.clicked.connect(self.openfilelocation)

        self.manageGui()

    def manageGui(self):
        """Manage gui"""



    def openfilelocation(self):
        """ Opens file location in native folder browser  """

        # http://stackoverflow.com/questions/6631299/python-opening-a-folder-in-explorer-nautilus-mac-thingie
        path = self.path
        # DEV: DELETE
        path = r"C:/"
        webbrowser.open(path)
        # if sys.platform == 'darwin':
        #     def openFolder(path):
        #         subprocess.check_call(['open', '--', path])
        # elif sys.platform == 'linux2':
        #     def openFolder(path):
        #         subprocess.check_call(['gnome-open', '--', path])
        # elif sys.platform == 'win32':
        #     def openFolder(path):
        #         subprocess.check_call(['explorer', path])