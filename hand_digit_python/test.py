import serial, time

arduino = serial.Serial('COM12', baudrate=9600, timeout=0.1)
time.sleep(1)

while True:
    print('Hi there!')
    var = int(input())
    if var == 1:
        arduino.write(b'1')
    if var == 2:
        arduino.write(b'2')
    if var == 3:
        arduino.write(b'3')
    if var == 4:
        arduino.write(b'4')
    if var == 5:
        arduino.write(b'5')

