#!/usr/bin/env python

import sys
import urllib, urllib2
from xml.etree import ElementTree

import gobject
gobject.threads_init()

import pygst
pygst.require("0.10")
import gst

print "Decoding audio"

bin = gst.parse_launch("filesrc name=source ! decodebin ! chromaprint name=chromaprint0 duration=60 ! fakesink sync=0 silent=TRUE")
source = bin.get_by_name("source")
source.set_property("location", sys.argv[1])

mainloop = gobject.MainLoop()

def on_eos(bus, msg):
   mainloop.quit()

bus = bin.get_bus()
bus.add_signal_watch()
bus.connect('message::eos', on_eos)

bin.set_state(gst.STATE_PLAYING)
mainloop.run()

format = gst.Format(gst.FORMAT_TIME)
length = bin.query_duration(format)[0] / gst.SECOND
bin.set_state(gst.STATE_NULL)

chromaprint = bin.get_by_name("chromaprint0")
fingerprint = chromaprint.get_property("fingerprint")

print "Looking up fingerprint"

data = {}
data['client'] = 'IUThVP5T'
data['meta'] = '2'
data['length'] = str(length)
data['fingerprint'] = fingerprint
resp = urllib2.urlopen('http://api.acoustid.org/lookup', urllib.urlencode(data))
tree = ElementTree.parse(resp)
results = tree.findall('results/result')
if results:
    print 'Found %s matching song(s):' % (len(results),)
    for result in results:
        print
        print 'Score:', result.find('score').text
        print 'ID:', result.find('id').text
        for track in result.findall('tracks/track'):
            print 'http://musicbrainz.org/track/%s.html' % track.find('id').text
else:
    print 'No matching songs found'

