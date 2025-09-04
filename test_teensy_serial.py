import platform
import serial
import serial.tools.list_ports
import time

print("running on ", platform.system())

def find_teensy_port():
    for port in serial.tools.list_ports.comports():
        # Teensy Vendor ID = 16c0 (decimal 5824), PJRC Product IDs vary (e.g., 0483 for Serial)
        if port.vid == 0x16C0:
            return port.device   # e.g. "COM3" or "/dev/ttyACM0"
    return None

teensy_port = find_teensy_port()

if teensy_port:
    print("Found Teensy on", teensy_port)
    ser = serial.Serial(teensy_port, 9600, timeout=1)
else:
    print("No Teensy found")
    exit(0)


ser = serial.Serial(teensy_port, 9600, timeout=1)
time.sleep(2)  # wait for Teensy to reset after opening port

ser.write(b'Hello Teensy!\n')
line = ser.readline().decode('utf-8').rstrip()
print("Received:", line)

ser.close()
