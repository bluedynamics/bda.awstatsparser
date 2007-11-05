from setuptools import setup, find_packages
import sys, os

version = '1.1'

setup(name='bda.awstatsparser',
      version=version,
      description="library for parsing of awstats result files",
      long_description="""""",
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
      ], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jens Klein',
      author_email='dev@bluedynamics.com',
      url='http://svn.plone.org/svn/collective/bda.awstatsparser/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup',]),
      namespace_packages=['bda',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',                        
          # -*- Extra requirements: -*
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
