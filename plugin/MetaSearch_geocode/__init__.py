# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2010 NextGIS (http://nextgis.org),
# Alexander Bruy (alexander.bruy@gmail.com),
# Maxim Dubinin (sim@gis-lab.info),
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

import os
import site
import sys


sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), "ui"))
sys.path.append("C:/Users/vesnikos/PycharmProjects/MetaSearch-dev/plugin/MetaSearch_geocode/pycharm-debug")
site.addsitedir(os.path.abspath('%s/ext-libs' % os.path.dirname(__file__)))


def classFactory(iface):
    """invoke plugin"""
    from plugin import MetaSearchPlugin
    return MetaSearchPlugin(iface)
