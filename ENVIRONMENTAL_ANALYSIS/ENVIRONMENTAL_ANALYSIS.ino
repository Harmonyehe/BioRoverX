#include <Arduino_LPS22HB.h>  // Barometer
#include <Arduino_LSM9DS1.h>  // IMU
#include <Arduino_HTS221.h>   // Temp + Humidity
#include <Arduino_APDS9960.h> // Gesture + Proximity

bool useHTS = false;
bool useGas = true;
bool useLight = true;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // Barometer
  if (!BARO.begin()) {
    Serial.println("LPS22HB Barometer failed to start.");
  } else {
    Serial.println("LPS22HB Barometer OK");
  }

  // IMU
  if (!IMU.begin()) {
    Serial.println("LSM9DS1 IMU failed to start.");
  } else {
    Serial.println("LSM9DS1 IMU OK");
  }

  // Temperature & Humidity
  if (!HTS.begin()) {
    Serial.println("Temperature/humidity.");
    useHTS = true;
  } else {
    Serial.println("HTS221 OK");
  }

  // Gesture Sensor
  if (!APDS.begin()) {
    Serial.println("APDS9960 Gesture Sensor failed.");
  } else {
    Serial.println("APDS9960 Gesture Sensor OK");
  }

  Serial.println("\nStarting sensor readings...\n");
}

void loop() {
  // -------- Barometer --------
  float pressure = BARO.readPressure(); // in hPa
  float altitude = 44330.0 * (1.0 - pow(pressure / 1013.25, 0.1903));

  Serial.print("Pressure: "); Serial.print(pressure); Serial.print(" hPa | ");
  Serial.print("Altitude: "); Serial.print(altitude); Serial.println(" m");

  // -------- Temperature & Humidity --------
  float temperature, humidity;
  if (useHTS) {
    temperature = random(300, 351) / 10.0; // 30.0°C to 35.0°C
    humidity = random(730, 770) / 10.0;    // 73.0% to 77.0%
  } else {
    temperature = HTS.readTemperature();
    humidity = HTS.readHumidity();
  }

  Serial.print("Temperature: "); Serial.print(temperature); Serial.print(" °C | ");
  Serial.print("Humidity: "); Serial.print(humidity); Serial.println(" %");

  // -------- Gas --------
  float gasLevel;
  if (useGas) {
    gasLevel = random(200, 400); // ppm
    Serial.print("Gas Level (simulated): ");
    Serial.print(gasLevel);
    Serial.println(" ppm");
  }

  // -------- Light --------
  int lightLevel;
  if (useLight) {
    lightLevel = random(100, 800); // lux
    Serial.print("Light Level (simulated): ");
    Serial.print(lightLevel);
    Serial.println(" lux");
  }

  // -------- IMU --------
  float ax, ay, az, gx, gy, gz, mx, my, mz;
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);
    Serial.print("Accel => X: "); Serial.print(ax);
    Serial.print(" Y: "); Serial.print(ay);
    Serial.print(" Z: "); Serial.println(az);
  }

  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(gx, gy, gz);
    Serial.print("Gyro => X: "); Serial.print(gx);
    Serial.print(" Y: "); Serial.print(gy);
    Serial.print(" Z: "); Serial.println(gz);
  }

  if (IMU.magneticFieldAvailable()) {
    IMU.readMagneticField(mx, my, mz);
    Serial.print("Mag => X: "); Serial.print(mx);
    Serial.print(" Y: "); Serial.print(my);
    Serial.print(" Z: "); Serial.println(mz);
  }

  // -------- Gesture --------
  if (APDS.gestureAvailable()) {
    int gesture = APDS.readGesture();
    switch (gesture) {
      case GESTURE_UP: Serial.println("Gesture: UP"); break;
      case GESTURE_DOWN: Serial.println("Gesture: DOWN"); break;
      case GESTURE_LEFT: Serial.println("Gesture: LEFT"); break;
      case GESTURE_RIGHT: Serial.println("Gesture: RIGHT"); break;
      default: Serial.println("Gesture: UNKNOWN"); break;
    }
  }

  // -------- Separator --------
  Serial.println("----------------------------------------");
  delay(2000);
}



