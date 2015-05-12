#!/usr/bin/python

import ephem
import sys
from time import gmtime, strftime

#get the current date with time
#get it from an external time module
date_time = strftime("%Y/%m/%d %H:%M:%S", gmtime())
print date_time

#get the current lat and lon
#get it from a gps dongle or an external gps module
#lat = '42.214559'
#lon = '-71.143653'

if (len(sys.argv) < 2):
    print "please enter the object name. ex: Mars"
    quit()

if (len(sys.argv) > 2) :
    lat = sys.argv[2]
    lon = sys.argv[3]
else:
    print "please enter latitude and longitude (lat first)"
    quit()

print lat
print lon

obs = ephem.Observer()
obs.lon = lon
obs.lat = lat
obs.date = date_time

arg = sys.argv[1]

result = getattr(ephem, arg)(obs)

print ('Right Ascension is: %s' % (result.ra))
print ('Declenation is: %s'% (result.dec))
print ('Altitude is: %s'%(result.alt))
print ('Azimuth is: %s'%(result.az))
