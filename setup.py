from distutils.core import setup
setup(name='bda-awstatsparser',
      packages=['bda', 'bda.awstatsparser'],
      package_dir={
        'bda': 'bda_parent',
        'bda.awstatsparser': '.'
      }
)
