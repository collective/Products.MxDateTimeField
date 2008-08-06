# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
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


import logging
logger = logging.getLogger('MxDateTimeField: setuphandlers')
from Products.MxDateTimeField.config import PROJECTNAME
from Products.MxDateTimeField.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
##/code-section HEAD

def isNotMxDateTimeFieldProfile(context):
    return context.readDataFile("MxDateTimeField_marker.txt") is None



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotMxDateTimeFieldProfile(context): return 
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()


def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotMxDateTimeFieldProfile(context): return 
    site = context.getSite()


##code-section FOOT
##/code-section FOOT
