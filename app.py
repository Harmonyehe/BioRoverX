from flask import Flask, render_template, Response
from picamera2 import Picamera2
import cv2
import time
import threading
import random

app = Flask(__name__)
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

frame = None

def capture_frames():
    global frame
    while True:
        image = picam2.capture_array()
        _, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        time.sleep(0.05)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sensors')
def sensors():
    temp = random.uniform(30.0, 35.0)
    hum = random.uniform(73.0, 77.0)
    pressure = random.uniform(950.0, 1020.0)
    light = random.randint(100, 800)
    gas = random.randint(200, 400)
    return {
        "temperature": f"{temp:.1f} °C",
        "humidity": f"{hum:.1f} %",
        "pressure": f"{pressure:.1f} hPa",
        "light": f"{light} lux",
        "gas": f"{gas} ppm"
    }

if __name__ == '__main__':
    t = threading.Thread(target=capture_frames)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=5000)

