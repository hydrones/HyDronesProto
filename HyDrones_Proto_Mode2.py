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
# HD = hd.Hydrones('COM3', 115200)


flagFixGPS = False
isDataFileOpen = False
startclock = dt.datetime.now()
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
        timetagGPS = (dt.datetime.now() - startclock).total_seconds()
        # Date convertion
        dateBuffer = str(gpsMeas['Year'])+'/'+str(gpsMeas['Month'])+'/'+str(gpsMeas['Day'])+' '+gpsMeas['Time']
        currentDate = dt.datetime.strptime(dateBuffer, "%y/%m/%d %H:%M:%S.%f")

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas01 = HD.doLeddarMeas()
        timetagLeddar01 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas02 = HD.doLeddarMeas()
        timetagLeddar02 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas03 = HD.doLeddarMeas()
        timetagLeddar03 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas04 = HD.doLeddarMeas()
        timetagLeddar04 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas05 = HD.doLeddarMeas()
        timetagLeddar05 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas06 = HD.doLeddarMeas()
        timetagLeddar06 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas07 = HD.doLeddarMeas()
        timetagLeddar07 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas08 = HD.doLeddarMeas()
        timetagLeddar08 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a barometer Measure"
        baroMeas01 = HD.doBaroMeas()
        timetagBaro01 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas09 = HD.doLeddarMeas()
        timetagLeddar09 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas10 = HD.doLeddarMeas()
        timetagLeddar10 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas11 = HD.doLeddarMeas()
        timetagLeddar11 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas12 = HD.doLeddarMeas()
        timetagLeddar12 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas13 = HD.doLeddarMeas()
        timetagLeddar13 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas14 = HD.doLeddarMeas()
        timetagLeddar14 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas15 = HD.doLeddarMeas()
        timetagLeddar15 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas16 = HD.doLeddarMeas()
        timetagLeddar16 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a IMU Measure"
        imuMeas01 = HD.doIMUMeas()
        timetagIMU01 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas17 = HD.doLeddarMeas()
        timetagLeddar17 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas18 = HD.doLeddarMeas()
        timetagLeddar18 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas19 = HD.doLeddarMeas()
        timetagLeddar19 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas20 = HD.doLeddarMeas()
        timetagLeddar20 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas21 = HD.doLeddarMeas()
        timetagLeddar21 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas22 = HD.doLeddarMeas()
        timetagLeddar22 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas23 = HD.doLeddarMeas()
        timetagLeddar23 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas24 = HD.doLeddarMeas()
        timetagLeddar24 = (dt.datetime.now() - startclock).total_seconds()




        # Struct data for the binary file
        structMeas = struct.Struct("<dH5BI3fIfdfIdfIdfIdfIdfIdfIdfIdfId4fdfIdfIdfIdfIdfIdfIdfIdfId12fdfIdfIdfIdfIdfIdfIdfIdfI")
        packedMeas = structMeas.pack(timetagGPS, \
                                     currentDate.year, \
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
                                     timetagLeddar01, \
                                     leddarMeas01['Range'], \
                                     leddarMeas01['Ampl'], \
                                     timetagLeddar02, \
                                     leddarMeas02['Range'], \
                                     leddarMeas02['Ampl'], \
                                     timetagLeddar03, \
                                     leddarMeas03['Range'], \
                                     leddarMeas03['Ampl'], \
                                     timetagLeddar04, \
                                     leddarMeas04['Range'], \
                                     leddarMeas04['Ampl'], \
                                     timetagLeddar05, \
                                     leddarMeas05['Range'], \
                                     leddarMeas05['Ampl'], \
                                     timetagLeddar06, \
                                     leddarMeas06['Range'], \
                                     leddarMeas06['Ampl'], \
                                     timetagLeddar07, \
                                     leddarMeas07['Range'], \
                                     leddarMeas07['Ampl'], \
                                     timetagLeddar08, \
                                     leddarMeas08['Range'], \
                                     leddarMeas08['Ampl'], \
                                     timetagBaro01, \
                                     baroMeas01['Pressure'], \
                                     baroMeas01['SeaLevelPressure'], \
                                     baroMeas01['Altitude'], \
                                     baroMeas01['Temperature'], \
                                     timetagLeddar09, \
                                     leddarMeas09['Range'], \
                                     leddarMeas09['Ampl'], \
                                     timetagLeddar10, \
                                     leddarMeas10['Range'], \
                                     leddarMeas10['Ampl'], \
                                     timetagLeddar11, \
                                     leddarMeas11['Range'], \
                                     leddarMeas11['Ampl'], \
                                     timetagLeddar12, \
                                     leddarMeas12['Range'], \
                                     leddarMeas12['Ampl'], \
                                     timetagLeddar13, \
                                     leddarMeas13['Range'], \
                                     leddarMeas13['Ampl'], \
                                     timetagLeddar14, \
                                     leddarMeas14['Range'], \
                                     leddarMeas14['Ampl'], \
                                     timetagLeddar15, \
                                     leddarMeas15['Range'], \
                                     leddarMeas15['Ampl'], \
                                     timetagLeddar16, \
                                     leddarMeas16['Range'], \
                                     leddarMeas16['Ampl'], \
                                     timetagIMU01, \
                                     imuMeas01['PitchAngle'], \
                                     imuMeas01['RollAngle'], \
                                     imuMeas01['YawAngle'], \
                                     imuMeas01['AccelX'], \
                                     imuMeas01['AccelY'], \
                                     imuMeas01['AccelZ'], \
                                     imuMeas01['LinearAccelX'], \
                                     imuMeas01['LinearAccelY'], \
                                     imuMeas01['LinearAccelZ'], \
                                     imuMeas01['GravAccelX'], \
                                     imuMeas01['GravAccelY'], \
                                     imuMeas01['GravAccelZ'], \
                                     timetagLeddar17, \
                                     leddarMeas17['Range'], \
                                     leddarMeas17['Ampl'], \
                                     timetagLeddar18, \
                                     leddarMeas18['Range'], \
                                     leddarMeas18['Ampl'], \
                                     timetagLeddar19, \
                                     leddarMeas19['Range'], \
                                     leddarMeas19['Ampl'], \
                                     timetagLeddar20, \
                                     leddarMeas20['Range'], \
                                     leddarMeas20['Ampl'], \
                                     timetagLeddar21, \
                                     leddarMeas21['Range'], \
                                     leddarMeas21['Ampl'], \
                                     timetagLeddar22, \
                                     leddarMeas22['Range'], \
                                     leddarMeas22['Ampl'], \
                                     timetagLeddar23, \
                                     leddarMeas23['Range'], \
                                     leddarMeas23['Ampl'], \
                                     timetagLeddar24, \
                                     leddarMeas24['Range'], \
                                     leddarMeas24['Ampl'])


        # Data record into binary files
        if (isDataFileOpen == False):
            startDate = currentDate
            fileName = "data/HD_mode2_"+startDate.strftime("%Y%m%d_%H%M%S%f")
            binaryFile = open(fileName, "wb")
            isDataFileOpen = True
        else:
            if ((currentDate - startDate) < dt.timedelta(minutes=1)):
                binaryFile.write(packedMeas)
            else:
                binaryFile.write(packedMeas)
                binaryFile.close()
                isDataFileOpen = False
