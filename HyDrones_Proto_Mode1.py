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

        # Send a command to the HyDrones Proto ==> "do a barometer Measure"
        baroMeas01 = HD.doBaroMeas()
        timetagBaro01 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas01 = HD.doLeddarMeas()
        timetagLeddar01 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas02 = HD.doLeddarMeas()
        timetagLeddar02 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas03 = HD.doLeddarMeas()
        timetagLeddar03 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas04 = HD.doLeddarMeas()
        timetagLeddar04 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a IMU Measure"
        imuMeas01 = HD.doIMUMeas()
        timetagIMU01 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas05 = HD.doLeddarMeas()
        timetagLeddar05 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas06 = HD.doLeddarMeas()
        timetagLeddar06 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas07 = HD.doLeddarMeas()
        timetagLeddar07 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas08 = HD.doLeddarMeas()
        timetagLeddar08 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a IMU Measure"
        imuMeas02 = HD.doIMUMeas()
        timetagIMU02 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a barometer Measure"
        baroMeas02 = HD.doBaroMeas()
        timetagBaro02 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas09 = HD.doLeddarMeas()
        timetagLeddar09 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas10 = HD.doLeddarMeas()
        timetagLeddar10 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas11 = HD.doLeddarMeas()
        timetagLeddar11 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas12 = HD.doLeddarMeas()
        timetagLeddar12 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a IMU Measure"
        imuMeas03 = HD.doIMUMeas()
        timetagIMU03 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas13 = HD.doLeddarMeas()
        timetagLeddar13 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas14 = HD.doLeddarMeas()
        timetagLeddar14 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas15 = HD.doLeddarMeas()
        timetagLeddar15 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas16 = HD.doLeddarMeas()
        timetagLeddar16 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a IMU Measure"
        imuMeas04 = HD.doIMUMeas()
        timetagIMU04 = (dt.datetime.now() - startclock).total_seconds()

        # Send a command to the HyDrones Proto ==> "do a leddar Measure"
        leddarMeas17 = HD.doLeddarMeas()
        timetagLeddar17 = (dt.datetime.now() - startclock).total_seconds()
        leddarMeas18 = HD.doLeddarMeas()
        timetagLeddar18 = (dt.datetime.now() - startclock).total_seconds()


        # Struct data for the binary file
        structMeas = struct.Struct("<dH5BI3fIfd4fdfIdfIdfIdfId12fdfIdfIdfIdfId12fd4fdfIdfIdfIdfId12fdfIdfIdfIdfId12fdfIdfI")
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
                                     timetagBaro01, \
                                     baroMeas01['Pressure'], \
                                     baroMeas01['SeaLevelPressure'], \
                                     baroMeas01['Altitude'], \
                                     baroMeas01['Temperature'], \
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
                                     timetagIMU02, \
                                     imuMeas02['PitchAngle'], \
                                     imuMeas02['RollAngle'], \
                                     imuMeas02['YawAngle'], \
                                     imuMeas02['AccelX'], \
                                     imuMeas02['AccelY'], \
                                     imuMeas02['AccelZ'], \
                                     imuMeas02['LinearAccelX'], \
                                     imuMeas02['LinearAccelY'], \
                                     imuMeas02['LinearAccelZ'], \
                                     imuMeas02['GravAccelX'], \
                                     imuMeas02['GravAccelY'], \
                                     imuMeas02['GravAccelZ'], \
                                     timetagBaro02, \
                                     baroMeas02['Pressure'], \
                                     baroMeas02['SeaLevelPressure'], \
                                     baroMeas02['Altitude'], \
                                     baroMeas02['Temperature'], \
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
                                     timetagIMU03, \
                                     imuMeas03['PitchAngle'], \
                                     imuMeas03['RollAngle'], \
                                     imuMeas03['YawAngle'], \
                                     imuMeas03['AccelX'], \
                                     imuMeas03['AccelY'], \
                                     imuMeas03['AccelZ'], \
                                     imuMeas03['LinearAccelX'], \
                                     imuMeas03['LinearAccelY'], \
                                     imuMeas03['LinearAccelZ'], \
                                     imuMeas03['GravAccelX'], \
                                     imuMeas03['GravAccelY'], \
                                     imuMeas03['GravAccelZ'], \
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
                                     timetagIMU04, \
                                     imuMeas04['PitchAngle'], \
                                     imuMeas04['RollAngle'], \
                                     imuMeas04['YawAngle'], \
                                     imuMeas04['AccelX'], \
                                     imuMeas04['AccelY'], \
                                     imuMeas04['AccelZ'], \
                                     imuMeas04['LinearAccelX'], \
                                     imuMeas04['LinearAccelY'], \
                                     imuMeas04['LinearAccelZ'], \
                                     imuMeas04['GravAccelX'], \
                                     imuMeas04['GravAccelY'], \
                                     imuMeas04['GravAccelZ'], \
                                     timetagLeddar17, \
                                     leddarMeas17['Range'], \
                                     leddarMeas17['Ampl'], \
                                     timetagLeddar18, \
                                     leddarMeas18['Range'], \
                                     leddarMeas18['Ampl'])

        # Data record into binary files
        if (isDataFileOpen == False):
            startDate = currentDate
            fileName = "data/HD_mode1_"+startDate.strftime("%Y%m%d_%H%M%S%f")
            binaryFile = open(fileName, "wb")
            isDataFileOpen = True
        else:
            if ((currentDate - startDate) < dt.timedelta(minutes=1)):
                binaryFile.write(packedMeas)
            else:
                binaryFile.write(packedMeas)
                binaryFile.close()
                isDataFileOpen = False
