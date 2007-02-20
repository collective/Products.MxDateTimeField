# -*- coding: utf-8 -*-
#
# File: MxDateTimeType.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.MxDateTimeField.MxDateTimeField import MxDateTimeField
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
        )
    ),

    MxDateTimeField(
        name='DateEnd',
        widget=MxDateTimeField._properties['widget'](
            label='Dateend',
            label_msgid='MxDateTimeField_label_DateEnd',
            i18n_domain='MxDateTimeField',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MxDateTimeType_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class MxDateTimeType(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'MxDateTimeType'

    meta_type = 'MxDateTimeType'
    portal_type = 'MxDateTimeType'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'MxDateTimeType.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "MxDateTimeType"
    typeDescMsgId = 'description_edit_mxdatetimetype'

    _at_rename_after_creation = True

    schema = MxDateTimeType_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(MxDateTimeType, PROJECTNAME)
# end of class MxDateTimeType

##code-section module-footer #fill in your manual code here
##/code-section module-footer



