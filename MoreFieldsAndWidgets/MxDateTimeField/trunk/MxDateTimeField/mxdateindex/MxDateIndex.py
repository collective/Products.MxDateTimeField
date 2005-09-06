# File: MxDateIndex.py
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


##code-section module-header #fill in your manual code here
from Globals import DTMLFile, InitializeClass
##/code-section module-header


from Products.PluginIndexes.DateIndex.DateIndex import DateIndex

class MxDateIndex(DateIndex):
    ''' '''
    __implements__ = (getattr(DateIndex,'__implements__',()),)

    ##code-section class-header_MxDateIndex #fill in your manual code here
    meta_type = "MxDateIndex"
    ##/code-section class-header_MxDateIndex

    def _convert( self, value, default=None ) :
        """Convert Date/Time value to our internal representation"""
        
        if type(value) == type('') :
            value = mx.DateTime.DateTimeFrom(value)
        
        if isinstance( value, mx.DateTime.mxDateTime.DateTimeType ):
            t_tup = value.tuple()
        else:
            return default

        yr = t_tup[0]
        mo = t_tup[1]
        dy = t_tup[2]
        hr = t_tup[3]
        mn = t_tup[4]

        t_val = ( ( ( ( yr * 12 + mo ) * 31 + dy ) * 24 + hr ) * 60 + mn )

        return t_val


##code-section module-footer #fill in your manual code here

InitializeClass( MxDateIndex )

def initialize(context):

    context.registerClass( \
            MxDateIndex,\
            permission='Add Pluggable Index', \
            constructors=(manage_addMxDateIndexForm,\
                          manage_addMxDateIndex),\
            icon='www/index.gif',\
            visibility=None\
            )

manage_addMxDateIndexForm = DTMLFile( 'dtml/addMxDateIndex', globals() )

def manage_addMxDateIndex( self, id, REQUEST=None, RESPONSE=None, URL3=None):
    """Add a MxDate index"""
    return self.manage_addIndex(id, 'MxDateIndex', extra=None, \
                    REQUEST=REQUEST, RESPONSE=RESPONSE, URL1=URL3)
##/code-section module-footer



