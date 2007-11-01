# -*- coding: utf-8 -*-
#
# Copyright (c) 2006 by Blue Dynamics Alliance Klein und Partner KEG Austria
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

__author__ = """Jens Klein <jens@bluedynamics.com>
                Robert Niederreiter <robertn@bluedynamcis.net>"""
__docformat__ = 'plaintext'

import os, sys
from utils import odict
import defaults

class ParsedSection(odict):
    """An ordered dict with integrated section parser."""
    
    def parse(self, rawdata, definition=None):  
        self.definiton = definition    
        for line in rawdata:
            line = line.strip()
            result = line.split()
            if definition is None or definition[1] is None:
                self[result[0]] = result[1:]
                continue
            resultdict = dict()
            for i in range(0 , len(result)):
                try:
                    resultdict[definition[i]] = result[i]
                except IndexError:
                    raise IndexError, 'index %s in %s' % (i, definition)
            self[result[0]] = resultdict
            

class ParsedMonth(dict):
    """An dict with integrated month parser. The key is the section name."""
        
    def parse(self, data, sectiondefs):
        """parses data and build sections"""
        data = data.split('\n')
        sname = None
        for i in range(0, len(data)-1):
            line = data[i].strip()
            if not line.startswith('BEGIN_'):
                continue
            name, length = line.split()
            name = name[6:]
            i += 1
            offset = i + int(length) -1
            rawsection = data[i:offset]
            self[name] = ParsedSection()
            self[name].parse(rawsection, sectiondefs.get(name, None))
            i += offset + 1
            
class ParsedStatistics(dict):
    """An dicts with integrated statistics parser. Keys are MMYYYY. it parses 
    the file on-demand."""
    
    def __init__(self, site, 
                 location, 
                 prefix=defaults.PREFIX, 
                 postfix=defaults.POSTFIX, 
                 sectiondefs=defaults.SECTIONDEFS,
                 absolutepath=True):
        dict.__init__(self)
        self.site = site
        if not location.startswith('/') and absolutepath:
            location = '/%s' % location
        self.location = location
        self.prefix = prefix
        self.postfix = postfix
        self.sectiondefs = sectiondefs
    
    def parseLogFile(self, my):
        """Parse a logfile from location on disk.
        
           my = month+year MMYYYY as string.
        """         
        filename = "%s%s.%s.%s" % (self.prefix, my, self.site, self.postfix)
        filename = os.path.join(self.location, filename)
        if not os.path.isfile(filename):
            print "%s does not exist" % filename
            return None
        f = open(filename)
        data = f.read()
        f.close()
        self[my] = ParsedMonth()
        self[my].parse(data, self.sectiondefs)
            
    
    def __getitem__(self, my):
        """"my = month+year MMYYYY as string."""
        if not my in self:
            self.parseLogFile(my)
        return self.get(my)

if __name__ == '__main__':
    from pprint import pprint
    ps = ParsedStatistics('www.yourdomain.com', 'data', absolutepath=False)
    pprint(ps['012007'])
