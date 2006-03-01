# File: test_dateindex.py
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

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) 
#

from Testing import ZopeTestCase
from Products.MxDateTimeField.tests.MxDateTestCase import MxDateTestCase

# Import the tested classes
from Products.MxDateTimeField.mxdateindex.MxDateIndex import MxDateIndex


class test_dateindex(MxDateTestCase):
    """ test-cases for class(es) 
    """

    ##code-section class-header_test_dateindex #fill in your manual code here
    ##/code-section class-header_test_dateindex

    def afterSetUp(self):
        """
        """
        pass

    # Manually created methods


def test_suite():
    from unittest import TestSuite
    from Testing.ZopeTestCase.zopedoctest import ZopeDocFileSuite

    ##code-section test-suite-in-between #fill in your manual code here
##/code-section test-suite-in-between


    return TestSuite((
        ZopeDocFileSuite('test_dateindex.txt',
                         package='Products.MxDateTimeField.doc',
                         test_class=test_dateindex),
    ))

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


