import serial
from time import sleep as delay
if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyAMA0", 115200, timeout= 1)
    ser.reset_input_buffer()
    count = 0
    while True:
         if ser.in_waiting > 0:
             line = ser.readline().decode('utf-8').rstrip()
             print(line)
         else if:
             ser.write("Hello From Raspberry Pi")
             delay(1)
             
