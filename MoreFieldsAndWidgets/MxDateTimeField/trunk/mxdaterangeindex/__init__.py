"""\
Initializes MxDateIndex for the zope catalog.

"""
# Copyright (c) 2005 by Bluedynamics KEG
# Generator: ArchGenXML Version 1.4 devel 1 http://sf.net/projects/archetypes/
#
# ZPL Zope Public Licence (ZPL)
# 
__author__  = '''Georg Gogo. BERNHARD <gogo@bluedynamics.com>'''
__docformat__ = 'plaintext'

DEBUG = True

from Products.MxDateTimeField.mxdaterangeindex import MxDateRangeIndex

def initialize(context):
    
    if DEBUG :
        print "*" * 200
        print ">> MxDateRangeIndex is being initialized."

    context.registerClass( \
            MxDateRangeIndex.MxDateRangeIndex,\
            permission='Add Pluggable Index', \
            constructors=(manage_addMxDateRangeIndexForm,\
                          manage_addMxDateRangeIndex),\
            icon='www/index.gif',\
            visibility=None\
            )
            
manage_addMxDateRangeIndexForm = MxDateRangeIndex.manage_addMxDateRangeIndexForm
manage_addMxDateRangeIndex     = MxDateRangeIndex.manage_addMxDateRangeIndex

