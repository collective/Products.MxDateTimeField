import mx.DateTime
from Products.PluginIndexes.DateIndex.DateIndex import DateIndex
from Globals import DTMLFile

class MxDateIndex(DateIndex) :
    
    meta_type = 'MxDateIndex'
    manage = manage_main = DTMLFile( 'dtml/manageMxDateIndex', globals() )
    manage_browse = DTMLFile('dtml/browseMxIndex', globals())
    
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

manage_addMxDateIndexForm = DTMLFile( 'dtml/addMxDateIndex', globals() )

def manage_addMxDateIndex( self, id, REQUEST=None, RESPONSE=None, URL3=None):
    """Add a MxDate index"""
    return self.manage_addIndex(id, 'MxDateIndex', extra=None, \
                    REQUEST=REQUEST, RESPONSE=RESPONSE, URL1=URL3)
                    
