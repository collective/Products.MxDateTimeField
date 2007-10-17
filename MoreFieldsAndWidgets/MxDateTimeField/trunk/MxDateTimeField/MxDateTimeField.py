# -*- coding: utf-8 -*-
#
# File: MxDateTimeField.py
#
# Copyright (c) 2007 by BlueDynamics Alliance, Bluedynamics KEG, Austria
# Generator: ArchGenXML Version 1.5.2
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

__author__ = """Georg Gogo. BERNHARD <gogo@bluedynamics.com>, Jens Klein
<jens@bluedynamics.com>"""
__docformat__ = 'plaintext'

#MxDateTimeField

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Field import ObjectField,encode,decode
from Products.Archetypes.Registry import registerField
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.Archetypes.Field  import *
from Products.Archetypes.Schema import Schema
try:
    from Products.generator import i18n
except ImportError:
    from Products.Archetypes.generator import i18n

from Products.MxDateTimeField import config

##code-section module-header #fill in your manual code here

import mx.DateTime.DateTime # egenix mx base is needed! Gogo.
from mx.DateTime import DateTimeType
from types import ListType, TupleType, StringTypes

from Products.CMFCore.utils import getToolByName
from Products.MxDateTimeField import config

DEBUG=0

##/code-section module-header
from Products.MxDateTimeField.MxDateTimeWidget import MxDateTimeWidget

class MxDateTimeField(ObjectField):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(ObjectField,'__implements__',()),)


    _properties = ObjectField._properties.copy()
    _properties.update({
        'type': 'mxdatetimefield',
        'widget':MxDateTimeWidget,
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()
    security.declarePrivate('set')
    security.declarePrivate('get')

    def set(self, instance, value, **kwargs):
      """
      Check if value is an actual date/time value. If not, attempt
      to convert it to one; otherwise, set to None. Assign all
      properties passed as kwargs to object.
      """
      if not value:
        value = None

      if type(value) in StringTypes:
        value = mx.DateTime.DateTimeFrom(value)

      if value and type(value) != DateTimeType:
          raise ValueError, "Argument to MxDateTimeField must be either a "+\
                            "string or a MxDateTime object, but "+\
                            "got: %s" % repr(value)

      ObjectField.set(self, instance, value, **kwargs)

registerField(MxDateTimeField,
              title='MxDateTimeField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



