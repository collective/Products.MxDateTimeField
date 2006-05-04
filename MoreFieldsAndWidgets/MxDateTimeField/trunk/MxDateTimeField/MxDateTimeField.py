# File: MxDateTimeField.py
#
# Copyright (c) 2006 by Bluedynamics KEG
# Generator: ArchGenXML Version 1.5.0 svn/devel
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
DEBUG = True
import mx.DateTime.DateTime # egenix mx base is needed! Gogo.
from mx.DateTime import DateTimeType
from types import ListType, TupleType, StringTypes

from Products.CMFCore.utils import getToolByName


from Products.MxDateTimeField import config

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

      if DEBUG :
        print "MxDateTimeField set method:", value, type(value)

      if not value:
        value = None

      if type(value) in StringTypes:
        if DEBUG :
          print "Setting value from string"
        value = mx.DateTime.DateTimeFrom(value)
        
      if value and type(value) != DateTimeType:
          raise ValueError,"argument to MxDateTimeField must be either a string or a MxDateTime object, but looks got: %s" % repr(value)

      ObjectField.set(self, instance, value, **kwargs)

    def getRaw(self, instance, **kwargs):
        val= ObjectField.get(self,instance,**kwargs)
        if val:
            return '%4d-%02d-%02d %02d:%02d:%02d' %(val.year,val.month,val.day,val.hour,val.minute,val.second)

        else:
            return None

    def get(self, instance, **kwargs):
        value = ObjectField.get(self, instance, **kwargs)
        return str(value)


registerField(MxDateTimeField,
              title='MxDateTimeField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



