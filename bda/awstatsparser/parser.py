# -*- coding: utf-8 -*-
# Copyright (c) 2006, 2010 by Blue Dynamics Alliance

import os, sys
from utils import odict
import defaults
import logging

logger = logging.getLogger('bda.awstatsparser')

class ParsedSection(odict):
    """An ordered dict with integrated section parser.
    """
    
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
    """An dict with integrated month parser. The key is the section name.
    """
        
    def parse(self, data, sectiondefs):
        """parses data and build sections.
        """
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
    the file on-demand.
    """
    
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
    
    @property
    def available(self):
        """List of available parsed stats keys.
        """
        ret = list()
        try:
            for file in os.listdir(self.location):
                if file.startswith(self.prefix) \
                  and file.endswith(self.postfix) \
                  and file.find(self.site) != -1:
                    idx = len(self.prefix)
                    ret.append(file[idx:idx + 6])
        except OSError, e:
            logger.error(str(e))
        return ret
    
    @property
    def latest(self):
        """Latest parsed stats key.
        """
        available = [(a[2:], a[:2]) for a in self.available]
        if not available:
            logger.warning("No parsed files found.")
            return None
        available = sorted(available, key=lambda x: (x[0], x[1]))
        return '%s%s' % (available[-1][1], available[-1][0])
    
    def parseLogFile(self, my):
        """Parse a logfile from location on disk.
        
        @param my: month+year MMYYYY as string.
        """         
        filename = "%s%s.%s.%s" % (self.prefix, my, self.site, self.postfix)
        filename = os.path.join(self.location, filename)
        if not os.path.isfile(filename):
            logger.error("%s does not exist" % filename)
            return None
        f = open(filename)
        data = f.read()
        f.close()
        self[my] = ParsedMonth()
        self[my].parse(data, self.sectiondefs)    
    
    def __getitem__(self, my):
        """@param my: month+year MMYYYY as string.
        """
        if not my in self:
            self.parseLogFile(my)
        return self.get(my)
    
    __repr__ = object.__repr__

if __name__ == '__main__':
    from pprint import pprint
    ps = ParsedStatistics('www.yourdomain.com', 'data', absolutepath=False)
    pprint(ps['012007'])
