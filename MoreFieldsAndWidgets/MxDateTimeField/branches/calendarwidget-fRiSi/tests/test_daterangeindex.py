# File: test_daterangeindex.py
#
# Copyright (c) 2006 by Bluedynamics KEG
# Generator: ArchGenXML Version 1.4.1 svn/devel
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
# test-cases for class(es) 
#
import os, sys
from Testing import ZopeTestCase
from Products.MxDateTimeField.tests.MxDateTestCase import MxDateTestCase
# import the tested classes
from Products.MxDateTimeField.mxdaterangeindex.MxDateRangeIndex import MxDateRangeIndex

class test_daterangeindex(MxDateTestCase):
    """ test-cases for class(es) 
    """

    ##code-section class-header_test_daterangeindex #fill in your manual code here
    ##/code-section class-header_test_daterangeindex

    def afterSetUp(self):
        """
        """
        pass


    # Manually created methods


def test_suite():
    from unittest import TestSuite
    from Testing.ZopeTestCase.zopedoctest import ZopeDocFileSuite

    return TestSuite((
        ZopeDocFileSuite('test_daterangeindex.txt',
                         package='Products.MxDateTimeField.doc',
                         test_class=test_daterangeindex),
    ))


##code-section module-footer #fill in your manual code here
##/code-section module-footer


if __name__ == '__main__':
    framework()


