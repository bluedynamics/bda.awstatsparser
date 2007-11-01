from setuptools import setup, find_packages
import sys, os

version = '1.0 (svn unreleased)'

setup(name='bda.awstatsparser',
      version=version,
      description="library for parsing awstats",
      long_description="""\
TODO""",
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Web Environment',
            'Framework :: Zope2',
            'License :: OSI Approved :: GNU General Public License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',            
      ], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jens Klein',
      author_email='dev@bluedynamics.com',
      url='',
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
