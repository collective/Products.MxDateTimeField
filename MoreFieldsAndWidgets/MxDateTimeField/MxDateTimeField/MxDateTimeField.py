# File: MxDateTimeField.py
# 
# Copyright (c) 2005 by Bluedynamics KEG
# Generator: ArchGenXML Version 1.4.0-beta2 devel 
#            http://plone.org/products/archgenxml
#
# GNU General Public Licence (GPL)
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#
__author__  = '''Georg Gogo. BERNHARD <gogo@bluedynamics.com>'''
__docformat__ = 'plaintext'

from types import ListType, TupleType, StringTypes
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
from Products.generator import i18n

from Products.MxDateTimeField import config

##code-section module-header #fill in your manual code here
DEBUG = False
import mx.DateTime.DateTime # egenix mx base is needed! Gogo.
from types import ListType, TupleType, StringTypes
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
from Products.generator import i18n

from Products.MxDateTimeField import config

##/code-section module-header

from MxDateTimeWidget import MxDateTimeWidget



class MxDateTimeField(ObjectField):
    ''' '''

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

      if type(value) == type('') :
        if DEBUG :
          print "Setting value from string"
        value = mx.DateTime.DateTimeFrom(value)

      ObjectField.set(self, instance, value, **kwargs)


registerField(MxDateTimeField,
              title='MxDateTimeField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



