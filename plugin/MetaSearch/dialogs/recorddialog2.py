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

from dateutil.parser import parse
from subprocess import check_call

from PyQt4.QtGui import QDialog, QPixmap
from PyQt4.QtCore import Qt

from MetaSearch.util import get_ui_class, open_url, ROI, get_resource

BASE_CLASS = get_ui_class('recorddialog2.ui')


class RecordDialog2(QDialog, BASE_CLASS):
    """Record Metadata Dialogue"""
    def __init__(self, record, iface):
        """
        :param record: <class 'owslib.csw.CswRecord'>
        """

        #QDialog.__init__(self)
        super(RecordDialog2, self).__init__()
        self.setupUi(self)
        self.iface = iface
        self.record = record
        self.roi = ROI(self.record, self)
        self.thumbnail = self.roi.get_thumbnail
        self.path = self.roi.local_folder_path
        self.tbOpenLocation.clicked.connect(self.openfilelocation)
        self.pixmap = QPixmap(get_resource("NoImage.png"))
        self.lblThumbnail.setPixmap(self.pixmap)
        self.btnAddWNSLayer.clicked.connect(self.create_wms_xml)

        self.uris = [uri for uri in self.record.uris]
        self.referenses = [reference for reference in self.record.references]

        self.manageGui()

    def manageGui(self):
        """Manage gui"""

        if self.path is not None:
            self.lePath.setText(str(self.path[0]))
            if len(self.path) > 1:  # More than one option
                # TODO: Add QCompleter
                pass
        else:
            self.tbOpenLocation.setEnabled(False)

        self.pteText.setPlainText(self.record.abstract)
        self.leTitle.setText(self.record.title)
        # dev stuff:
        for i in self.uris:
            self.pteText.appendPlainText(str(i)+"\n")
        for i in self.referenses:
            self.pteText.appendPlainText(str(i)+"\n")
        self.pteText.appendPlainText(self.record.date)
        if self.pixmap.load(self.thumbnail[0], self.thumbnail[1]):
            self.pixmap.scaled(self.lblThumbnail.maximumWidth(),
                               self.lblThumbnail.maximumHeight(),
                               Qt.KeepAspectRatio)
            self.lblThumbnail.setPixmap(self.pixmap)

        self.set_lblDate()

    def set_lblDate(self):
        date = parse(self.record.date)
        intro = self.tr("Last Modified:")
        strdate = "%s/%s/%s %s:%s" % (date.day, date.month, date.year,
                                      date.hour, date.minute)
        self.lblDate.setText(" ".join([intro, strdate]))

    def openfilelocation(self):
        """ Opens file location in native folder browser  """

        path = self.lePath.text()
        open_url(path)

    def create_wms_xml(self):
        p = check_call(["gdalinfo", "--version"])