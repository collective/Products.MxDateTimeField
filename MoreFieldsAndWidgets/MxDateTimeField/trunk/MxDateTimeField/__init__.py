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


# There are three ways to inject custom code here:
#
#   - To set global configuration variables, create a file AppConfig.py.
#       This will be imported in config.py, which in turn is imported in
#       each generated class and in this file.
#   - To perform custom initialisation after types have been registered,
#       use the protected code section at the bottom of initialize().
#   - To register a customisation policy, create a file CustomizationPolicy.py
#       with a method register(context) to register the policy.

from zLOG import LOG, INFO

LOG('MxDateTimeField',INFO, 'Installing Product')

try:
    import CustomizationPolicy
except ImportError:
    CustomizationPolicy = None

from Globals import package_home
from Products.CMFCore import utils as cmfutils
from Products.CMFCore import CMFCorePermissions
from Products.CMFCore import DirectoryView
from Products.CMFPlone.PloneUtilities import ToolInit
from Products.Archetypes.atapi import *
from Products.Archetypes import listTypes
from Products.Archetypes.utils import capitalize

import os, os.path

from Products.MxDateTimeField.config import *

DirectoryView.registerDirectory('skins', product_globals)
DirectoryView.registerDirectory('skins/MxDateTimeField',
                                    product_globals)

##code-section custom-init-head #fill in your manual code here
from Products.MxDateTimeField.mxdateindex import MxDateIndex
from Products.MxDateTimeField.mxdaterangeindex import MxDateRangeIndex
##/code-section custom-init-head


def initialize(context):
    ##code-section custom-init-top #fill in your manual code here
    MxDateIndex.initialize(context)
    MxDateRangeIndex.initialize(context)
    ##/code-section custom-init-top

    # imports packages and types for registration
    import mxdateindex
    import mxdaterangeindex
    import testclasses

    import MxDateTimeField
    import MxDateTimeWidget

    # Initialize portal content
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    cmfutils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)

    # Apply customization-policy, if theres any
    if CustomizationPolicy and hasattr(CustomizationPolicy, 'register'):
        CustomizationPolicy.register(context)
        print 'Customization policy for MxDateTimeField installed'

    ##code-section custom-init-bottom #fill in your manual code here
    ##/code-section custom-init-bottom

