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

from dateutil.parser import  parse

from PyQt4.QtGui import QDialog, QPixmap

from MetaSearch.util import get_ui_class, open_url, ROI, get_resource

BASE_CLASS = get_ui_class('recorddialog2.ui')


class RecordDialog2(QDialog, BASE_CLASS):
    """Record Metadata Dialogue"""
    def __init__(self, record):
        """
        :param record: <class 'owslib.csw.CswRecord'>
        """

        #QDialog.__init__(self)
        super(RecordDialog2, self).__init__()
        self.record = record
        self.roi = ROI(self.record, self)
        self.setupUi(self)
        self.path = self.roi.local_folder
        self.tbOpenLocation.clicked.connect(self.openfilelocation)

        self.pixmap = QPixmap(get_resource("NoImage.png"))
        self.lblThumbnail.setPixmap(self.pixmap)

        self.uris = [uri for uri in self.record.uris]
        self.referenses = [reference for reference in self.record.references]

        self.manageGui()

    def manageGui(self):
        """Manage gui"""

        if self.path is not None:
            self.lePath.setText(str(self.path))

        self.pteText.setPlainText(self.record.abstract)
        self.leTitle.setText(self.record.title)
        for i in self.uris:
            self.pteText.appendPlainText(str(i)+"\n")
        for i in self.referenses:
            self.pteText.appendPlainText(str(i)+"\n")
        self.pteText.appendPlainText(self.record.created)
        self.pteText.appendPlainText(self.record.modified)
        self.pteText.appendPlainText(self.record.date)
        self.set_lblDate()


    def set_lblDate(self):
        date = parse(self.record.date)
        self.lblDate.setText("%s/%s/%s %s:%s" % (date.day, date.month, date.year, date.hour, date.minute))


    def openfilelocation(self):
        """ Opens file location in native folder browser  """

        # http://stackoverflow.com/questions/6631299/python-opening-a-folder-in-explorer-nautilus-mac-thingie
        # TODO: take the file path from lePath
        path = self.path
        open_url(path)
