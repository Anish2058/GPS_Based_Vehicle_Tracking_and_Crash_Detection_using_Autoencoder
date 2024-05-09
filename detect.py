import RPi.GPIO as GPIO
import time
import serial
import board
import busio
from adafruit_mpu6050 import MPU6050
import numpy as np
from tensorflow.keras.models import load_model
import requests
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)         # Buzzer
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button with pull-up resistor

account_sid = 'AC4b402edaaf2fa7e7cdf9e8a31293ca54'
auth_token = '328632e984e2d4932bb8ca8fa7c17f37'
client = Client(account_sid, auth_token)

url = 'http://192.168.18.206:5000/update_map/'

model = load_model('./crashdetection2.h5')
batch_size = 10
data_lines = []

seq_size = 5
def to_sequences(x, seq_size=1):
    x_values = []
    for i in range(len(x)-seq_size+1):
        x_values.append(x[i:i+seq_size])
    return x_values

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = MPU6050(i2c)

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

try:
    while True:
        x, y, z = accelerometer.acceleration

        x = (x - 0.02585581) / 0.79294326
        y = (y - 0.11246101) / 0.72514735
        z = (z - 9.77259644) / 0.84326735

        data = [x, y, z]
        data_lines.append(data)

        if len(data_lines) >= batch_size:
            prediction_data = to_sequences(data_lines, seq_size)

            prediction = model.predict(prediction_data)
            errorMAE = np.mean(np.abs(prediction - prediction_data), axis=1)
            anomalies = errorMAE > 3
            print(np.sum(anomalies))

            if np.sum(anomalies) >= 1:
                GPIO.output(5, GPIO.HIGH)
                start_time = time.time()
                while time.time() - start_time < 5:
                    print("checking")
                    if GPIO.input(6) == GPIO.LOW:
                        GPIO.output(5, GPIO.LOW)
                        print("pressed button")
                        break

                if GPIO.input(6) == GPIO.LOW:
                    print(anomalies)
                    print('accident detected')
                    message = client.messages.create(
                        from_='+14157671713',
                        body='Accident Alert',
                        to='+977xxxxxxxxxx'
                    )

                GPIO.cleanup()
                break

            data_lines = []

        try:
            line = ser.readline().decode('utf-8').strip()
            if line.startswith('$GPGGA'):
                fields = line.split(',')
                latitude = fields[2]
                degree = latitude[:2]
                minute = latitude[2:]
                longitude = fields[4]
                degreel = longitude[:3]
                minutel = longitude[3:]
                if degree:
                    latitude_decimal = int(degree) + float(minute) / 60
                    longitude_decimal = int(degreel) + float(minutel) / 60
                    data = {'latitude': latitude_decimal, 'longitude': longitude_decimal}
                    print(data)
                    response = requests.post(url, json=data)
                    time.sleep(0.1)
        except serial.SerialException:
            print("GPS module disconnected. Proceeding without GPS data...")

except KeyboardInterrupt:
    print("Program terminated by user.")

ser.close()