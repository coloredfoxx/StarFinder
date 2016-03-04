#!/usr/bin/python
import os
from gps import *

time = None
latitude = None
longitude = None
altitude = None
attempts = 0

session=gps(mode=WATCH_ENABLE)

while attempts < 10:
    try:
        report=session.next()
        attempts += 1

        if report['class'] == 'TPV':
            session.close()
            session = gps(mode=WATCH_ENABLE)
            time = report.time
            latitude = report.lat
            longitude = report.lon
            altitude = report.alt

    except (KeyboardInterrupt, StopIteration):
        print "GPSD has terminated"
