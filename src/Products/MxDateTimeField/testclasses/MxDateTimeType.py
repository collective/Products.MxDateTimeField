# -*- coding: utf-8 -*-
#
# File: MxDateTimeType.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.MxDateTimeField.MxDateTimeField import MxDateTimeField
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.MxDateTimeField.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    MxDateTimeField(
        name='DateBegin',
        widget=MxDateTimeField._properties['widget'](
            label='Datebegin',
            label_msgid='MxDateTimeField_label_DateBegin',
            i18n_domain='MxDateTimeField',
        ),
    ),
    MxDateTimeField(
        name='DateEnd',
        widget=MxDateTimeField._properties['widget'](
            label='Dateend',
            label_msgid='MxDateTimeField_label_DateEnd',
            i18n_domain='MxDateTimeField',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MxDateTimeType_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class MxDateTimeType(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IMxDateTimeType)

    meta_type = 'MxDateTimeType'
    _at_rename_after_creation = True

    schema = MxDateTimeType_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(MxDateTimeType, PROJECTNAME)
# end of class MxDateTimeType

##code-section module-footer #fill in your manual code here
##/code-section module-footer



