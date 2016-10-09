#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial

class Hydrones(object):

    def __init__(self, port, baudrate=115200):
        """
        Initialize the serial port for USB communication.

        Input:
            - port: on which the HyDrones prototype is plugged
            - baudrate: speed of the communication (default: 115200)
        """
        self.ser = serial.Serial(port, baudrate)

    def __str__(self):
        """
        Just print the __init__ result.
        """
        return "Arduino is on port %s at %d baudrate" %(self.ser.port, self.ser.baudrate)

    def doLeddarMeas(self):
        """
        Perform a leddar measurement by sending the "doLeddarMeas" command to the
        HyDrones prototype.

        Output:
            - dictionary {'Ampl': signal amplitude, 'Range': range distance measurement(m)}
        """
        self.__sendCmd("doLeddarMeas")
        leddarOutput = self.__getData()
        if "leddarMeas" in leddarOutput:
            amplitude = int(leddarOutput.split('/')[1])
            altiRange = float(leddarOutput.split('/')[2])/1000.0
            leddarMeas = {'Ampl':amplitude, 'Range': altiRange}
            return leddarMeas
        else:
            leddarMeas = {'Ampl': 99999.0, 'Range': 99999.0}
            return leddarMeas

    def doGPSFix(self):
        """
        Wait for the GPS fix.
        !!! HAS TO BE CALLED ONCE PER SECOND MAXIMUM !!!

        Output:
            - Flag giving the status of the GPS: True = fix OK, False = No fix
        """
        self.__sendCmd("doGPSFix")
        initGPSOutput = self.__getData()
        flagInitGPS = False
        if 'fixGPS' in initGPSOutput:
            if 'True' in initGPSOutput.split('/')[1]:
                flagInitGPS = True
                return flagInitGPS
            else:
                return flagInitGPS

    def doGPSMeas(self):
        """
        Perform a GPS measurement only if the initGPS method has returned a 'True' value.
        !!! HAS TO BE CALLED ONCE PER SECOND MAXIMUM !!!

        Output:
            - dictionary {'Year': year, 'Month': month, 'Day': day, 'Time': HH:MM:SS.sss, 'Latitude': latitude, 'Longitude': longitude, 'Altitude': hauteur au dessus du niveau de la mer}
        """
        self.__sendCmd("doGPSMeas")
        gpsOuput = self.__getData()
        if "gpsMeas" in gpsOuput:
            gpsYear = int(gpsOuput.split('/')[1])
            gpsMonth = int(gpsOuput.split('/')[2])
            gpsDay = int(gpsOuput.split('/')[3])
            gpsTime = gpsOuput.split('/')[4]
            gpsLat = float(gpsOuput.split('/')[5])
            gpsLon = float(gpsOuput.split('/')[6])
            gpsGeoid = float(gpsOuput.split('/')[7])
            gpsNbSat = int(gpsOuput.split('/')[8])
            gpsAlt = float(gpsOuput.split('/')[9])
            gpsMeas = {'Year': gpsYear, 'Month': gpsMonth, 'Day': gpsDay, 'Time': gpsTime, 'Latitude': gpsLat, 'Longitude': gpsLon, 'GeoidHeight': gpsGeoid, 'NbSat': gpsNbSat,'Altitude': gpsAlt}
            return gpsMeas
        else:
            gpsMeas = {'Year': 99, 'Month': 99, 'Day': 99, 'Time': "99:99:99.999", 'Latitude': 99999.0, 'Longitude': 99999.0, 'GeoidHeight': 99999.0, 'NbSat': 99, 'Altitude': 99999.0}
            return gpsMeas


    def doIMUMeas(self):
        """
        Perform an IMU measurement by sending the "doIMUMeas" command to the
        HyDrones prototype.

        Output:
            - dictionary {'PitchAngle': pitch angle (deg), 'RollAngle': roll angle (deg), 'LinearAccelX': linear acceleration along the X-axis (m/s-2), 'LinearAccelY': linear acceleration along the Y-axis (m/s-2), 'LinearAccelZ': linear acceleration along the Z-axis (m/s-2)}
        """
        self.__sendCmd("doIMUMeas")
        imuOutput = self.__getData()
        if "imuMeas" in imuOutput:
            pitchAngle = float(imuOutput.split('/')[1])
            rollAngle = float(imuOutput.split('/')[2])
            yawAngle = float(imuOutput.split('/')[3])
            accelX = float(imuOutput.split('/')[4])
            accelY = float(imuOutput.split('/')[5])
            accelZ = float(imuOutput.split('/')[6])
            linearAccelX = float(imuOutput.split('/')[7])
            linearAccelY = float(imuOutput.split('/')[8])
            linearAccelZ = float(imuOutput.split('/')[9])
            gravAccelX = float(imuOutput.split('/')[10])
            gravAccelY = float(imuOutput.split('/')[11])
            gravAccelZ = float(imuOutput.split('/')[12])
            imuMeas = {'PitchAngle': pitchAngle, 'RollAngle': rollAngle, 'YawAngle': yawAngle, 'AccelX': accelX, 'AccelY': accelY, 'AccelZ': accelZ, 'LinearAccelX': linearAccelX, 'LinearAccelY': linearAccelY, 'LinearAccelZ': linearAccelZ, 'GravAccelX': gravAccelX, 'GravAccelY': gravAccelY, 'GravAccelZ': gravAccelZ}
            return imuMeas
        else:
            imuMeas = {'PitchAngle': 99999.0, 'RollAngle': 99999.0, 'YawAngle': 99999.0, 'AccelX': 99999.0, 'AccelY': 99999.0, 'AccelZ': 99999.0, 'LinearAccelX': 99999.0, 'LinearAccelY': 99999.0, 'LinearAccelZ': 99999.0, 'GravAccelX': 99999.0, 'GravAccelY': 99999.0, 'GravAccelZ': 99999.0}
            return imuMeas

    def doBaroMeas(self):
        """
        Perform a barometer measurement by sending the "doBaroMeas" command to the
        HyDrones prototype.

        Output:
            - dictionary {'Pressure': current pressure in Pa, 'SeaLevelPressure': pressure at sea level in Pa, 'Atltitude': altitude in m, 'Temperature': temperature in degree C}
        }
        """
        self.__sendCmd("doBaroMeas")
        baroOutput = self.__getData()
        if "baroMeas" in baroOutput:
            pressure = float(baroOutput.split("/")[1])
            seaLevelPressure = float(baroOutput.split("/")[2])
            altitude = float(baroOutput.split("/")[3])
            temperature = float(baroOutput.split("/")[4])
            baroMeas = {'Pressure': pressure, 'SeaLevelPressure': seaLevelPressure, 'Altitude': altitude, 'Temperature': temperature}
            return baroMeas
        else:
            baroMeas = {'Pressure': 99999.0, 'SeaLevelPressure': 99999.0, 'Atltitude': 99999.0, 'Temperature': 99999.0}
            return baroMeas

    def __sendCmd(self, command):
        """
        Send a command to the HyDrones prototype by writing a string to the serial port.

        Input:
            - command: String containing the HyDrones prototype command
        """
        self.ser.flushInput()
        self.ser.flushOutput()
        serialcmd = str(command)+"zz"
        self.ser.write(serialcmd.encode())

    def __getData(self):
        """
        Read the data on the serial port sent by the HyDrones prototype.

        Output:
            - string sent by the HyDrones prototype on the usb serial port
        """
        self.ser.inWaiting()
        outputData = self.ser.readline().decode()
        return outputData

    def close(self):
        """
        Close the serial port.
        """
        self.ser.close()
        return True
