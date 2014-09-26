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
__author__ = 'vesnikos'
__date__ = '24/09/2014'

from PyQt4.QtCore import *
from PyQt4.QtGui import QLineEdit


class mLineEdit(QLineEdit):
    """ Test Custom Widget """

    def __init__(self, *args):
        QLineEdit.__init__(self, *args)
        self.ignore = False

    @staticmethod
    def ignore(self):
        return self.ignore

    def event(self, event):
        if (event.type() == event.KeyPress) and \
                (event.key() == Qt.Key_Backspace):
            self.ignore = True
        else:
            self.ignore = False
        return QLineEdit.event(self, event)
