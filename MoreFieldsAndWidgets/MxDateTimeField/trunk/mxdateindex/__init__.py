"""\
Initializes MxDateRangeIndex for the zope catalog.

"""
# Copyright (c) 2005 by Bluedynamics KEG
# Generator: ArchGenXML Version 1.4 devel 1 http://sf.net/projects/archetypes/
#
# ZPL Zope Public Licence (ZPL)
# 
__author__  = '''Georg Gogo. BERNHARD <gogo@bluedynamics.com>
                 Jens Klein <jens.klein@bluedynamics.com>'''
__docformat__ = 'plaintext'

DEBUG = True

from Products.MxDateTimeField.mxdateindex import MxDateIndex

def initialize(context):

    if DEBUG :
        print ">> MxDateIndex is being initialized."
    
    context.registerClass( \
            MxDateIndex.MxDateIndex,\
            permission='Add Pluggable Index', \
            constructors=(manage_addMxDateIndexForm,\
                          manage_addMxDateIndex),\
            icon='www/index.gif',\
            visibility=None\
            )

manage_addMxDateIndexForm = MxDateIndex.manage_addMxDateIndexForm
manage_addMxDateIndex     = MxDateIndex.manage_addMxDateIndex

