#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Code de test le plus bete du monde




# Librairies:
# -----------
import time
import libHydrones as hd
import datetime as dt
import struct


HD = hd.Hydrones('/dev/ttyACM0', 115200)

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

        # Struct data for the binary file
        structMeas = struct.Struct("<HBBBBBIfffIffIfffffffff")
        packedMeas = structMeas.pack(currentDate.year, \
                                     currentDate.month, \
                                     currentDate.day, \
                                     currentDate.hour, \
                                     currentDate.minute, \
                                     currentDate.second, \
                                     currentDate.microsecond, \
                                     gpsMeas['Latitude'], \
                                     gpsMeas['Longitude'], \
                                     gpsMeas['GeoidHeight'], \
                                     gpsMeas['NbSat'], \
                                     gpsMeas['Altitude'], \
                                     leddarMeas['Range'], \
                                     leddarMeas['Ampl'], \
                                     baroMeas['Pressure'], \
                                     baroMeas['SeaLevelPressure'], \
                                     baroMeas['Altitude'], \
                                     baroMeas['Temperature'], \
                                     imuMeas['PitchAngle'], \
                                     imuMeas['RollAngle'], \
                                     imuMeas['LinearAccelX'], \
                                     imuMeas['LinearAccelY'], \
                                     imuMeas['LinearAccelZ'])

        # Data record into binary files
        if (isDataFileOpen == False):
            startDate = currentDate
            fileName = "data/HD_test_"+startDate.strftime("%Y%m%d_%H%M%S%f")
            binaryFile = open(fileName, "wb")
            isDataFileOpen = True
        else:
            if ((currentDate - startDate) < dt.timedelta(minutes=1)):
                binaryFile.write(packedMeas)
            else:
                binaryFile.write(packedMeas)
                binaryFile.close()
                isDataFileOpen = False
