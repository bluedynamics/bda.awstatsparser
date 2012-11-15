Usage
=====

This egg contains a parser for ``AwStats`` files, providing a convenient
``dict`` like API::

    >>> from bda.awstatsparser.defaults import (
    ...     PREFIX,
    ...     POSTFIX,
    ...     SECTIONDEFS,
    ... )

``PREFIX`` and ``POSTFIX`` are used to build the target stats file path,
``SECTIONDEFS`` defines the expected structure of the stats file and the keys
to use for providing the several values.

The API is provided due to the ``ParsedStatistics`` class::

    >>> from bda.awstatsparser.parser import ParsedStatistics
    >>> parser = ParsedStatistics(domain='same_as_awstats_conf_name',
    ...                           dir='/var/lib/awstats',
    ...                           PREFIX, POSTFIX, SECTIONDEFS)

You can ask for ``available`` stats keys::

    >>> parser.available
    ['012010', '122009']

You can query the ``latest`` available stats key::

    >>> parser.latest
    '012010'

Access some stats information::

    >>> sider = parser[parser.latest]['SIDER']
    >>> stat = sider['/path/which/was/logged']
    >>> stat['pages']
    99


Contributors
============

- Jens Klein <jens@bluedynamics.com>

- Robert Niederreiter <rnix@squarewave.at>
