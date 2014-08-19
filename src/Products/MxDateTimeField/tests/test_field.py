# -*- coding: utf-8 -*-
#
# File: test_field.py
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

import os, sys
try:
    from Products.PloneTestCase.PloneTestCase import USELAYER
    from Products.PloneTestCase.layer import PloneSite
except:
    USELAYER = False
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) MxDateTimeType
#

from Testing import ZopeTestCase
from Products.MxDateTimeField.tests.MxDateTestCase import MxDateTestCase

# Import the tested classes
from Products.MxDateTimeField.testclasses.MxDateTimeType import MxDateTimeType


class test_field(MxDateTestCase):
    """ test-cases for class(es) 
    """

    ##code-section class-header_test_field #fill in your manual code here
    ##/code-section class-header_test_field

    def afterSetUp(self):
        """
        """
        pass
    # Manually created methods
    # Manually created methods


def test_suite():
    from unittest import TestSuite
    from Testing.ZopeTestCase.zopedoctest import ZopeDocFileSuite
    from Testing.ZopeTestCase import ZopeDocFileSuite
    ##code-section test-suite-in-between #fill in your manual code here
##/code-section test-suite-in-between


    s = ZopeDocFileSuite('test_field.txt',
                         package='Products.MxDateTimeField.doc',
                         test_class=test_field)
    if USELAYER:
        s.layer = PloneSite
    return TestSuite((s,
                      ))

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


