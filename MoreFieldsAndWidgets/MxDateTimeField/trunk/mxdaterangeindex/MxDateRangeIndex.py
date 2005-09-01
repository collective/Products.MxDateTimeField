import mx.DateTime
from Products.PluginIndexes.DateRangeIndex.DateRangeIndex import DateRangeIndex
from Globals import DTMLFile, InitializeClass

class MxDateRangeIndex(DateRangeIndex):

    meta_type = "MxDateRangeIndex"

    def _convertDateTime( self, value ):
        if value is None:
            return value
        if type( value ) == type( '' ):
            value = mx.DateTime.DateTimeFrom( value )
        result = int(value.ticks() / 1000 / 60) # flatten to minutes
        return result

    manage_indexProperties = DTMLFile( 'dtml/manageMxDateRangeIndex', globals() )
        
        
InitializeClass( MxDateRangeIndex )

manage_addMxDateRangeIndexForm = DTMLFile( 'dtml/addMxDateRangeIndex', globals() )

def manage_addMxDateRangeIndex(self, id, extra=None,
        REQUEST=None, RESPONSE=None, URL3=None):
    """
        Add a MxDateRangeIndex to the catalog, using the incredibly icky
        double-indirection-which-hides-NOTHING.
    """
    return self.manage_addIndex(id, 'MxDateRangeIndex', extra,
        REQUEST, RESPONSE, URL3)
        
