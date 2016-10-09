#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Code de test le plus bete du monde




# Librairies:
# -----------
import time
import libHydrones as hd
import datetime as dt
import struct


# HD = hd.Hydrones('/dev/ttyACM0', 115200)
HD = hd.Hydrones('COM3', 115200)

flagFixGPS = False
isDataFileOpen = False
while True:

    # Initialize the GPS signal until the satellite's hooking
    while (flagFixGPS != True):
        flagFixGPS = HD.doGPSFix()
        if (flagFixGPS):
            print("GPS Fix OK")
        else:
            print("Waiting for GPS Fix")
        time.sleep(1.0)

    # Start HyDrones Measure if fix GPS = OK
    if (flagFixGPS):

        now = dt.datetime.now()

        # Send a command to the HyDrones Proto ==> "do a GPS Measure"
        gpsMeas = HD.doGPSMeas()

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas = HD.doLeddarMeas()

        # Send a command to the HyDrones Proto ==> "do a barometer Measure"
        baroMeas = HD.doBaroMeas()

        # Send a command to the HyDrones Proto ==> "do a IMU Measure"
        imuMeas = HD.doIMUMeas()

        # Date convertion
        dateBuffer = str(gpsMeas['Year'])+'/'+str(gpsMeas['Month'])+'/'+str(gpsMeas['Day'])+' '+gpsMeas['Time']
        currentDate = dt.datetime.strptime(dateBuffer, "%y/%m/%d %H:%M:%S.%f")


        # Print results
        print("GPS=> Date: %d/%d/%d %s, Lat: %f, Lon: %f, GeoidHeight: %f, NbSat: %d, Altitude: %f m" % (gpsMeas['Day'], gpsMeas['Month'], gpsMeas['Year'], gpsMeas['Time'], gpsMeas['Latitude'], gpsMeas['Longitude'], gpsMeas['GeoidHeight'], gpsMeas['NbSat'], gpsMeas['Altitude']))
        print("Leddar=> Amplitude: %f, Distance: %f m"% (leddarMeas['Ampl'], leddarMeas['Range']))
        print("Barometer=> Pressure: %f Pa, Pressure at sea level: %f Pa, Altitude: %f m, Temperature: %f C" % (baroMeas['Pressure'], baroMeas['SeaLevelPressure'], baroMeas['Altitude'], baroMeas['Temperature']))
        print("IMU Angle=> Pitch angle: %f deg, Roll angle: %f deg, Yaw angle: %f deg"% (imuMeas['PitchAngle'], imuMeas['RollAngle'], imuMeas['YawAngle']))
        print("IMU Accel=> Axel X: %f m/s-2, Accel Y: %f m/s-2, Accel Z: %f m/s-2"% (imuMeas['AccelX'], imuMeas['AccelY'], imuMeas['AccelZ']))
        print("IMU Linear Accel=> Linear Axel X: %f m/s-2, Linear Accel Y: %f m/s-2, Linear Accel Z: %f m/s-2"% (imuMeas['LinearAccelX'], imuMeas['LinearAccelY'], imuMeas['LinearAccelZ']))
        print("IMU Gravity Accel=> Gravity Axel X: %f g, Gravity Accel Y: %f g, Gravity Accel Z: %f g"% (imuMeas['GravAccelX'], imuMeas['GravAccelY'], imuMeas['GravAccelZ']))
        # print(now)
        print("-----------------------\n")
