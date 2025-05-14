import serial
import time

# Adjust this to your serial port (check with `ls /dev/ttyACM*`)
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200
LOG_FILE = 'sensor_log.csv'

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)  # Wait for Arduino to reset

with open(LOG_FILE, 'a') as file:
    print("Logging started... Press CTRL+C to stop.")
    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            print(line)
            file.write(line + '\n')
    except KeyboardInterrupt:
        print("Logging stopped.")
