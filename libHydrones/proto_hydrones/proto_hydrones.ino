
/*
proto_hydrones
--------------
Language: Arduino

Arduino firmware for managing 
the Hydrones prototype:
* Leddar ==> Serial3
* Inertial Measurement Unit (IMU) ==> direct plug
* GPS ==> Serial2
* barometer ==> I2C SDA/SCL (20/21)

Created 05 Aug. 2016
by Jean-Christophe Poisson
*/

#include <Leddar.h>
#include <Adafruit_GPS.h>
#include <Adafruit_BMP085.h>
#include <Wire.h>
#include <NAxisMotion.h>




#ifndef SERIAL_RATE
#define SERIAL_RATE         115200
#endif

#ifndef SERIAL_TIMEOUT
#define SERIAL_TIMEOUT      5
#endif



// ======================
// - HyDrones Functions -
// ======================

// Read command
// ------------
String readCmd() {
  while(1) {
    if (Serial.available() > 0){
      String cmd = Serial.readStringUntil('zz');
      Serial.flush();
      return cmd;
    }
  }
}




// Do Leddar measurement
// ---------------------
String doLeddarMeas(LeddarOne Leddar) {

  unsigned int distance = 0;
  unsigned int amplitude = 0;
  
  if (Leddar.getDetections() >= 0) {
    
    // For the moment, only the first detection is considered
    distance = Leddar.Detections[0].Distance;
    amplitude = Leddar.Detections[0].Amplitude;
    
    // Send results on the usb serial port
    String leddarBuffer = "leddarMeas/" + String(amplitude, DEC) + "/" + String(distance, DEC);
    return leddarBuffer;
  }
  else {
    String leddarBuffer = "leddarMeas/99999.0/99999.0";
    return leddarBuffer;
  }
}


// Do the GPS fix
// ---------------
String doGPSFix(Adafruit_GPS GPS) {
  
  // Empty the GPS serial buffer
  bool newData = false;
  while(Serial2.available() > 0) Serial2.read();
  
  // Read GPS output until a complete sentence  
  while (!newData) {
    char c = GPS.read();
    if (GPS.newNMEAreceived() && GPS.parse(GPS.lastNMEA())) {
      newData = true;
    }
  }
  
  if (GPS.fix) {
      return String("fixGPS/True");
  }
  else {
    return String("fixGPS/False");
  }
}


// Do GPS Measurement (date, Lat, Lon and altitude)
// ------------------------------------------------
String doGPSMeas(Adafruit_GPS GPS) {
  
  bool newData = false;
  
  float flat = 0.0;
  float flon = 0.0;
  int year = 0;
  int month = 0;
  int day = 0;
  int hour = 0;
  int minute = 0; 
  int seconds = 0;
  int milliseconds = 0;
  float geoidHeight = 0.0;
  int nbSat = 0;
  float alt = 0.0;
  
  // Empty the GPS serial buffer
  while(Serial2.available() > 0) Serial2.read();
  
  // Read GPS output until a complete sentence  
  while (!newData) {
    char c = GPS.read();
    if (GPS.newNMEAreceived() && GPS.parse(GPS.lastNMEA()) && GPS.fix) {
      newData = true;
    }
  }
  
  // Read GPS measure
  if (newData) {
    year = int(GPS.year);
    month = int(GPS.month);
    day = int(GPS.day);
    hour = int(GPS.hour);
    minute = int(GPS.minute);
    seconds = int(GPS.seconds);
    milliseconds = int(GPS.milliseconds);
    flat = float(GPS.latitudeDegrees);
    flon = float(GPS.longitudeDegrees);
    geoidHeight = float(GPS.geoidheight);
    nbSat = int(GPS.satellites);
    alt = float(GPS.altitude);
    
    // Send results on the usb serial port
    String gpsBuffer = "gpsMeas/" 
                     + String(year) 
                     +"/"+ String(month) 
                     +"/"+ String(day) 
                     +"/"+ String(hour) +":"+ String(minute) +":"+ String(seconds) +"."+ String(milliseconds)
                     +"/"+ String(flat, DEC)
                     +"/"+ String(flon, DEC)
                     +"/"+ String(geoidHeight, DEC)
                     +"/"+ String(nbSat)
                     +"/"+ String(alt, DEC);
    return gpsBuffer;
  }
  else {
    // Send results on the usb serial port
    String gpsBuffer = "gpsMeas/" 
                     + String("99")
                     +"/"+ "99"
                     +"/"+ "99"
                     +"/"+ "99:99:99.999"
                     +"/"+ "99999.0"
                     +"/"+ "99999.0"
                     +"/"+ "99999.0"
                     +"/"+ "99"
                     +"/"+ "99999.0";
    return gpsBuffer;
  }    
}


// Do Barometer measuremment (Temp, Pressure, altitude)
// ----------------------------------------------------
String doBaroMeas(Adafruit_BMP085 BARO) {
  
  // Initialization
  unsigned long start = millis();
  int nbMeas = 0;
  float meanTemperature = 0.0;
  float meanPressure = 0.0;
  float meanSeaLevelPressure = 0.0;
  float meanAltitude = 0.0;
  
  // Do Measurements during 200 ms
  while (millis() - start < 200) {
    meanPressure += BARO.readPressure();
    meanSeaLevelPressure += BARO.readSealevelPressure();
    meanAltitude += BARO.readAltitude();
    meanTemperature += BARO.readTemperature();
    nbMeas += 1;
    // read measurements every 10 ms
    delay(10);
  }
  
  // Compute average values
  meanPressure = meanPressure / nbMeas;
  meanSeaLevelPressure = meanSeaLevelPressure / nbMeas;
  meanAltitude = meanAltitude / nbMeas;
  meanTemperature = meanTemperature / nbMeas;

  // Send results on the usb serial port
  String baroBuffer = "baroMeas/"
                    + String(meanPressure, DEC)
                    +"/"+ String(meanSeaLevelPressure, DEC)
                    +"/"+ String(meanAltitude, DEC)
                    +"/"+ String(meanTemperature, DEC);
  return baroBuffer;
}


// Do IMU measurement (pitch and roll)
// -----------------------------------
String doIMUMeas(NAxisMotion IMU) {
  
  float pitchAngle = 0.0;
  float rollAngle = 0.0;
  float linearAccelX = 0.0;
  float linearAccelY = 0.0;
  float linearAccelZ = 0.0;
  
  // Update the Euler data into the object
  IMU.updateEuler();
  
  // Read Pitch and Roll angle measurements
  pitchAngle = IMU.readEulerPitch();
  rollAngle = IMU.readEulerRoll();
  
  // Update Linear Acceleration data into the object
  IMU.updateAccel();
  IMU.updateLinearAccel();
  
  // Read linear acceleration in the 3 directions
  linearAccelX = IMU.readLinearAccelX();
  linearAccelY = IMU.readLinearAccelY();
  linearAccelZ = IMU.readLinearAccelZ();
  
  // Send results on the usb serial port
  String imuBuffer = "imuMeas/" 
                   + String(pitchAngle, DEC) 
                   + "/" + String(rollAngle, DEC)
                   + "/" + String(linearAccelX, DEC)
                   + "/" + String(linearAccelY, DEC)
                   + "/" + String(linearAccelZ, DEC);
  return imuBuffer;  
}



// ================
// - Main Program -
// ================

// Leddar Object: Baudrate = 115200, Modbus slave ID = 01, TX3/RX3 
LeddarOne Leddar1(115200, 1, Serial3);

// GPS object
#define GPSSerial Serial2
Adafruit_GPS GPS(&GPSSerial);
#define GPSECHO false

// Barometer object
Adafruit_BMP085 BARO;

// IMU object:
NAxisMotion IMUsensor;

     
void setup(){
  // Initialize Leddar
  Leddar1.init();
  
  // Prepare for GPS
  GPS.begin(9600); // The AdaFruit GPS works at 9600bds
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ); // 1 Hz update rate
  delay(1000);
  
  // Initialize I2C
  I2C.begin();
  
  // Initialize Barometer
  BARO.begin();
  
  // Initialize IMU sensor
  IMUsensor.initSensor();
  IMUsensor.setOperationMode(OPERATION_MODE_NDOF);
  IMUsensor.setUpdateMode(MANUAL);
  
  // Initialize serial usb
  Serial.begin(SERIAL_RATE);
  Serial.setTimeout(SERIAL_TIMEOUT);
  Serial.println("InitSerial");
}


void loop(){
    
  // Command reading sent by the PC
  String input = readCmd();
  String leddarBuffer = "";
  String imuBuffer = "";
  String fixGPSBuffer = "";
  String gpsBuffer = "";
  String baroBuffer = "";
  
  // Analyze and execute command
  if (input == "doLeddarMeas") {
    leddarBuffer = doLeddarMeas(Leddar1);
    Serial.flush();
    Serial.println(leddarBuffer);
  }
  else if (input == "doIMUMeas") {
    imuBuffer = doIMUMeas(IMUsensor);
    Serial.flush();
    Serial.println(imuBuffer);
  }
  else if (input == "doGPSFix") {
    fixGPSBuffer = doGPSFix(GPS);
    Serial.flush();
    Serial.println(fixGPSBuffer);
  }
  else if (input == "doGPSMeas") {
    gpsBuffer = doGPSMeas(GPS);
    Serial.flush();
    Serial.println(gpsBuffer);
  }
  else if (input == "doBaroMeas") {
    baroBuffer = doBaroMeas(BARO);
    Serial.flush();
    Serial.println(baroBuffer);
  }
  
}
  
  


