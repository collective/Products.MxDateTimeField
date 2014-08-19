from setuptools import setup, find_packages
import os

version = '1.1'
shortdesc = 'Archetypes Field using MxDateTime'

longdesc = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.rst')
    ).read()

setup(
    name='Products.MXDateTimeField',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        "Framework :: Plone",
    ],
    keywords='',
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    license='GPLv2',
    url='https://pypi.python.org/pypi/collective.pfg.soup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
