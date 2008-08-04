===============
MxDateTimeField
===============
  
  This field enables Archetypes to use mxDateTime fields. It is very simple,
  it just transforms (well formed) strings into mxDateTime values. You can use
  the Field in Archetypes schemas like this:
  
  ...
  
  from Products.MxDateTimeField import MxDateTimeField
  
  ...
  
  schema= Schema((
    MxDateTimeField('BirthDate',
    ),
    
  ...
  
  The benefit of the MxDateTimeField is that a wider range of time designations
  is supported, dates may range from 5'000'000CE to 5'000'000BCE. Sometimes
  you encounter Problems in Plone when you want to use such dates.
  
  
Installation
  
  You need to install egenix mxDateTime first, it is part of 'mxBase', see 
  http://www.egenix.com/files/python/eGenix-mx-Extensions.html#Download-mxBASE

  Several Operating Systems are offering the egenix mxDateTime within their 
  package management systems.
  
  Then just put the MxDateTime folder into your Zopes 'Products' directory. 
  The Product should be listed among your Zopes Products in the control panel.
  
  
Thanks
  
  Thanks to Philipp Auersperg and Jens Klein for their hints and tips and
  for AGX ;-)
  
  
Links 
  
  Read more about mxDateTime - Date and Time types for Python:
  http://www.egenix.com/files/python/mxDateTime.html
  
  Visit Bluedynamice:
  http://www.bluedynamics.com
  
  See my Homepage:
  http://gogo.bluedynamics.com
  
  
Support
  
  If you have any questionns feel free to ask!
  
  irc: irc.freenode.net #bluedynamics
  email: gogo@bluedynamics.com
  
  
Author
  
  Georg Gogo. BERNHARD
  gogo@bluedynamics.com
  
 
GNU General Public Licence (GPL).
 
  This program is free software; you can redistribute it and/or modify it under
  the terms of the GNU General Public License as published by the Free Software
  Foundation; either version 2 of the License, or (at your option) any later
  version.

  This program is distributed in the hope that it will be useful, but WITHOUT
  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
  details.

  You should have received a copy of the GNU General Public License along with
  this program; if not, write to the Free Software Foundation, Inc., 59 Temple
  Place, Suite 330, Boston, MA  02111-1307  USA
 
