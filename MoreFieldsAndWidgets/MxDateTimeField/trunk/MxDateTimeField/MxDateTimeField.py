# -*- coding: utf-8 -*-
#
# File: MxDateTimeField.py
#
# Copyright (c) 2008 by BlueDynamics Alliance, Bluedynamics KEG, Austria
# Generator: ArchGenXML Version 2.2 (svn)
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
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

from zope.interface import implements
from Products.MxDateTimeField.MxDateTimeWidget import MxDateTimeWidget
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin





class MxDateTimeField(ObjectField):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header



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



