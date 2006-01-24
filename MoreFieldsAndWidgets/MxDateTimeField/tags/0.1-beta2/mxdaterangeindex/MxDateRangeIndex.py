# File: MxDateRangeIndex.py
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


from Products.PluginIndexes.DateRangeIndex.DateRangeIndex import DateRangeIndex

class MxDateRangeIndex(DateRangeIndex):
    ''' '''
    __implements__ = (getattr(DateRangeIndex,'__implements__',()),)

    ##code-section class-header_MxDateRangeIndex #fill in your manual code here
    meta_type = "MxDateRangeIndex"
    ##/code-section class-header_MxDateRangeIndex






    def _convertDateTime( self, value ):
        if value is None:
            return value
        if type( value ) == type( '' ):
            value = mx.DateTime.DateTimeFrom( value )
        result = int(value.ticks() / 1000 / 60) # flatten to minutes
        return result


##code-section module-footer #fill in your manual code here

def initialize(context):

    context.registerClass( \
            MxDateRangeIndex,\
            permission='Add Pluggable Index', \
            constructors=(manage_addMxDateRangeIndexForm,\
                          manage_addMxDateRangeIndex),\
            icon='www/index.gif',\
            visibility=None\
            )


InitializeClass( MxDateRangeIndex )

manage_addMxDateRangeIndexForm = DTMLFile( 'dtml/addMxDateRangeIndex', globals() )
manage_indexProperties = DTMLFile( 'dtml/manageMxDateRangeIndex', globals() )

def manage_addMxDateRangeIndex(self, id, extra=None,
        REQUEST=None, RESPONSE=None, URL3=None):
    """
        Add a mx date range index to the catalog, using the incredibly icky
        double-indirection-which-hides-NOTHING.
    """
    return self.manage_addIndex(id, 'MxDateRangeIndex', extra,
        REQUEST, RESPONSE, URL3)


##/code-section module-footer



