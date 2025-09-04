import serial
import time

# On Windows, this might have been "COM3"
# On Raspberry Pi/Linux, it's usually /dev/ttyACM0
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # wait for Teensy to reset after opening port

ser.write(b'Hello Teensy!\n')
line = ser.readline().decode('utf-8').rstrip()
print("Received:", line)

ser.close()
