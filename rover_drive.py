import RPi.GPIO as GPIO
import cv2
import time
import numpy as np

# ==== GPIO Setup ====
in1 = 17
in2 = 27
in3 = 23
in4 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in [in1, in2, in3, in4]:
    GPIO.setup(pin, GPIO.OUT)

def stop():
    GPIO.output(in1, 0)
    GPIO.output(in2, 0)
    GPIO.output(in3, 0)
    GPIO.output(in4, 0)

def forward():
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)

def backward():
    GPIO.output(in1, 0)
    GPIO.output(in2, 1)
    GPIO.output(in3, 0)
    GPIO.output(in4, 1)

def turn_left():
    GPIO.output(in1, 0)
    GPIO.output(in2, 1)
    GPIO.output(in3, 1)
    GPIO.output(in4, 0)

def turn_right():
    GPIO.output(in1, 1)
    GPIO.output(in2, 0)
    GPIO.output(in3, 0)
    GPIO.output(in4, 1)

# ==== Camera Setup ====
cap = cv2.VideoCapture(0)  # Use Pi Camera
cap.set(3, 320)  # Width
cap.set(4, 240)  # Height

print("Starting obstacle avoidance. Press Ctrl+C to stop.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera error.")
            break

        # Convert to HSV for color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define red color range for obstacle detection
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)
        red_pixels = cv2.countNonZero(mask)

        # Obstacle logic
        if red_pixels > 500:
            print("Obstacle detected! Stopping.")
            stop()
            time.sleep(1)
            turn_right()
            time.sleep(0.5)
            stop()
        else:
            print("Clear path. Moving forward.")
            forward()

        # (Optional) show the frame
        # cv2.imshow("Frame", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

except KeyboardInterrupt:
    print("\nStopped by user")

finally:
    stop()
    cap.release()
    GPIO.cleanup()
    # cv2.destroyAllWindows()
