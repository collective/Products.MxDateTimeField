# File: MxDateTimeWidget.py
#
# Copyright (c) 2006 by Bluedynamics KEG
# Generator: ArchGenXML Version 1.4.1 svn/devel
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Georg Gogo. BERNHARD <gogo@bluedynamics.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.Widget import TypesWidget

from types import ListType, TupleType, StringTypes
from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Field import ObjectField,encode,decode
from Products.Archetypes.Registry import registerField
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.generator import i18n

from Products.MxDateTimeField import config

##code-section module-header #fill in your manual code here
##/code-section module-header



class MxDateTimeWidget(TypesWidget):
    ''' '''

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(TypesWidget,'__implements__',()),)

    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : 'MxDateTimeWidget',
        'size' : '30',
        'maxlength' : '255',
        ##code-section widget-properties #fill in your manual code here
        ##/code-section widget-properties

        })

    security = ClassSecurityInfo()




##code-section module-footer #fill in your manual code here
##/code-section module-footer







