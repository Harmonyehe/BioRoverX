BioRoverX: Autonomous Mobile BioLab Assistant for Extreme Environments
BioRoverX is an autonomous mobile robotic platform designed to collect and analyze environmental data in harsh or extreme environments. The rover is equipped with a 6-DOF robotic arm for sample collection and path clearing, as well as a suite of environmental sensors for data collection. The system is powered by a Raspberry Pi 5 and Arduino Nano 33 BLE Sense, with a focus on TinyML for low-power operation and efficient environmental condition classification.

Features
Autonomous Navigation: The rover uses four OG555 motors controlled by an L298N motor driver for movement.


6-DOF Robotic Arm: Mounted on the rover for sample collection and path clearing.


Environmental Sensors:


Arduino Nano 33 BLE Sense: Measures temperature, humidity, pressure, light intensity, and motion (via accelerometer, gyroscope).


Gas Sensor, pH Sensor, Spectral Sensor (planned for future integration).


Machine Learning: Environmental data is processed by machine learning models running on the Raspberry Pi to predict environmental conditions.


Real-time Imaging: A 5MP Raspberry Pi camera is used for object detection and monitoring.


TinyML: Data is processed efficiently to minimize power consumption, and all critical data is saved locally and to the cloud.


Automatic Robotic Arm Trigger: The arm is activated when anomalies or specific conditions are detected by the sensors.


Hardware Components
Raspberry Pi 5: The central processing unit for controlling the rover and running machine learning models.


Arduino Nano 33 BLE Sense: Handles sensor data collection (temperature, humidity, pressure, light, motion).


OG555 Motors: 4 motors for driving the rover.


L298N Motor Driver: Controls the motors.


6-DOF Robotic Arm: Performs sample collection and path clearing.


5MP Raspberry Pi Camera: Provides real-time imaging for environmental monitoring.


Sensors:


Temperature, Humidity, Pressure, Light, IMU (Accelerometer & Gyroscope).


Future integration of gas, pH, and spectral sensors.


Software
Raspberry Pi OS: The operating system running on the Raspberry Pi 5.


Arduino IDE: Used to program the Arduino Nano 33 BLE Sense for sensor data collection.


TinyML: Models trained for environmental condition prediction and power optimization.


Python: Used for controlling the Raspberry Pi, processing data, and running machine learning models.


OpenCV: For real-time object detection using the Raspberry Pi camera.


Cloud Storage: For uploading environmental data and snapshots for remote monitoring.


Installation and Setup
Prerequisites
Raspberry Pi 5 (with Raspberry Pi OS installed)


Arduino Nano 33 BLE Sense


6-DOF robotic arm


L298N Motor Driver


OG555 motors


5MP Raspberry Pi camera


Environmental sensors (Temperature, Humidity, Pressure, Light, Motion)


Setting Up the Raspberry Pi
Install Raspberry Pi OS on your Raspberry Pi 5.


Set up the Python environment and required libraries:

 pip install opencv-python tensorflow


Install TinyML tools and configure the necessary models.


Connect the 5MP Camera and ensure it's accessible in Python with OpenCV.


Setting Up the Arduino Nano 33 BLE Sense
Install the Arduino IDE and select the Arduino Nano 33 BLE Sense board.


Upload the sensor data collection sketch to the Arduino Nano 33 BLE Sense.


Wiring the Motors
Connect the OG555 motors to the L298N motor driver for movement control.


Wire the motor driver to the Raspberry Pi GPIO pins.


Testing
Run the following command on the Raspberry Pi to check if the robotic arm and rover motors work as expected:

 python test_rover.py


Usage
Power On: Turn on the Raspberry Pi and Arduino Nano 33 BLE Sense.


Run the Rover: The rover will automatically start its mission after initializing the sensors and systems.


Monitor Data: View the real-time environmental data and images from the Raspberry Pi camera through the cloud storage.


Future Work
Integration of gas, pH, and spectral sensors for enhanced environmental analysis.


Improvement of machine learning models for better accuracy and prediction.


Expansion of the robotic arm's capabilities to support more complex sample collection tasks.


License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments
Special thanks to the TinyML community for their support in building the low-power machine learning models.


Thanks to the Raspberry Pi Foundation and Arduino for their incredible platforms.

![PT2 REPORT BIOROVERX Image 55](https://github.com/user-attachments/assets/0881c0e5-43ea-43e3-b17d-70134011d288)
![side view](https://github.com/user-attachments/assets/2eacee20-e787-4c4b-8e32-a0ce722ace68)
![front view](https://github.com/user-attachments/assets/36365def-4a80-474c-8bd4-a3ab7adbe189)


https://github.com/user-attachments/assets/c9a7881d-07e0-486f-b08b-c897be450523


