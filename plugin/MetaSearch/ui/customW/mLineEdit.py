# -*- coding: utf-8 -*-
__author__ = 'vesnikos'
__date__ = '24/09/2014'

from PyQt4.QtCore import *
from PyQt4.QtGui import QLineEdit, QWidget

class mLineEdit(QLineEdit):
    """ Test Custom Widget """



    def __init__(self, *args):
        QLineEdit.__init__(self,*args)
        self.ignore = False

    @staticmethod
    def ignore(self):
        return self.ignore

    def event(self, QEvent):
        if (QEvent.type()== QEvent.KeyPress) and (QEvent.key()==Qt.Key_Backspace):
            self.ignore = True
            #print "FUCK YOU"
        if QEvent.type()== QEvent.KeyRelease:
            self.ignore = False
            #print "FUCK YOU TOO"
        return QLineEdit.event(self,QEvent)
