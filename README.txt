Usage
=====

This egg contains a parser for ``AwStats`` files, providing a convenient
``dict`` like API.
::

    >>> from bda.awstatsparser.defaults import (
    ...     PREFIX,
    ...     POSTFIX,
    ...     SECTIONDEFS,
    ... )

``PREFIX`` and ``POSTFIX`` are used to build the target stats file path,
``SECTIONDEFS`` defines the expected structure of the stats file and the keys
to use for providing the several values.

The API is provided due to the ``ParsedStatistics`` class.
::
    
    >>> from bda.awstatsparser.parser import ParsedStatistics
    >>> parser = ParsedStatistics(domain='same_as_awstats_conf_name',
    ...                           dir='/var/lib/awstats',
    ...                           PREFIX, POSTFIX, SECTIONDEFS)

You can ask for ``available`` stats keys.
::

    >>> parser.available
    ['012010', '122009']

You can query the ``latest`` available stats key.
::

    >>> parser.latest
    '012010'

Access some stats information.
::

    >>> sider = parser[parser.latest]['SIDER']
    >>> stat = sider['/path/which/was/logged']
    >>> stat['pages']
    99

Changes
=======

1.2.1 - unreleased
  * fixed bug "When parsing a section, it leaves off the last line of the 
    section.". Thanks to Mike Hansen for report and patch. 2010-04-18 - jensens

1.2.0
  * added ``available`` property. 2010-01-26 - rnix
  * added ``latest`` property. 2010-01-26 - rnix
  * added logger and log some warnings and errors. 2010-01-26 - rnix

1.1
  * released on pypi 2007-11-05 - jensens

1.0
  * initial work - rnix, jensens

Contributors
============

  * Jens Klein <jens@bluedynamics.com>
  * Robert Niederreiter <rnix@squarewave.at>
