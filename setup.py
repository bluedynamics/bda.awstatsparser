import os
from setuptools import (
    setup,
    find_packages,
)


version = '1.2.1'
shortdesc = 'Library for parsing of awstats result files'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(name='bda.awstatsparser',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
      keywords='plone statistics',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url="http://pypi.python.org/pypi/bda.awstatsparser",
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['bda'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'odict',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """)
