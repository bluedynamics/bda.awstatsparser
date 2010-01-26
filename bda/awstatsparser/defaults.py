# -*- coding: utf-8 -*-
# Copyright (c) 2006, 2010 by Blue Dynamics Alliance

PREFIX = 'awstats'
POSTFIX= 'txt'

# Defines AWStats default sections:
#     'SECTION': [meaning of key, names for values or None to keep it a list]
SECTIONDEFS = {
    'MAP' : ['section', 'offset'],
    'GENERAL': ['key', None],
    'TIME': ['hour', 'pages', 'hits', 'bandwidth', 'not viewed pages', 'not viewed hits', 'not viewed bandwidth'],
    'VISITOR': ['host', 'pages', 'hits', 'bandwidth', 'last visit date', 'start date of last visit', 'last page of last visit'],            
    'DAY': ['date', 'pages', 'hits', 'bandwidth', 'visits'],
    'DOMAIN': ['domain', 'pages', 'hits', 'bandwidth'],
    'LOGIN': ['cluster id', 'pages', 'hits', 'bandwidth', 'last visit date'],
    'ROBOT': ['robot id', 'hits', 'bandwidth', 'last visit', 'hits on robots.txt'],     
    'WORMS': ['worm id', 'hits', 'bandwidth', 'last visit'],     
    'EMAILSENDER': ['email', 'hits', 'bandwidth', 'last visit'],   
    'EMAILRECEIVER': ['email', 'hits', 'bandwidth', 'last visit'],     
    'SESSION': ['session range', 'number of visits'],      
    'SIDER': ['url', 'pages', 'bandwidth', 'entry', 'exit'],      
    'FILETYPES': ['files type', 'hits', 'bandwidth', 'bandwidth without compression', 'bandwidth after compression'],
    'OS': ['os id', 'hits'],   
    'BROWSER': ['browser id', 'hits'],
    'SCREENSIZE': ['screen size', 'hits'],
    'UNKNOWNREFERER': ['unknown referer os', 'last visit date'],
    'UNKNOWNREFERERBROWSER': ['unknown referer browser', 'last visit date'],
    'ORIGIN': ['origin', 'pages', 'hits'],
    'SEREFERRALS': ['search engine referers id', 'pages', 'hits'],
    'PAGEREFS': ['external page referers', 'pages', 'hits'], 
    'SEARCHWORDS': ['search keyphrases', 'number of search'],
    'KEYWORDS': ['search keyword', 'number of search'],      
    'MISC': ['misc id', 'pages', 'hits', 'bandwidth'],          
    'ERRORS': ['errors', 'hits', 'bandwidth'],       
    'CLUSTER': ['cluster id', 'pages', 'hits', 'bandwidth'],      
    'SIDER_404': ['urls with 404 errors', 'hits', 'last url referer'],
}