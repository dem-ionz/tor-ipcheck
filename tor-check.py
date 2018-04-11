#!/usr/bin/env python
  """
  This is built specifically for ipchicken.com to check to see if Tor
  or any other socks 5 proxy is working.
  """
import re
import socks
import socket
import urllib2

def _filter_array(array):
        '''Returns an array of unique values.'''
        unique = {}
        for item in array:
            unique[item] = 1
        return unique.keys()

meh = "http://www.ipchicken.com/"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

req = urllib2.Request(meh, headers=hdr)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

content = page.read()

ip = re.findall( r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content)
results = _filter_array(ip)
for i in results:
    print i
