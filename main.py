#!/usr/bin/python
import ephem
import sys
from time import gmtime, strftime
from gps_data import *

#get the current date with time
time=str(time)
date_time=time.replace('T',' ')[:-5]
#degug message
#print date_time,'\n',latitude,'\n',longitude,'\n',altitude

if (len(sys.argv) < 2):
    print "please enter the object name argument. ex: 'python main.py Mars'"
    quit()

obs = ephem.Observer()
obs.lon = longitude
obs.lat = latitude
obs.date = date_time

arg = sys.argv[1]

result = getattr(ephem, arg)(obs)

print ('Right Ascension is: %s' % (result.ra))
print ('Declenation is: %s'% (result.dec))
print ('Altitude is: %s'%(result.alt))
print ('Azimuth is: %s'%(result.az))
