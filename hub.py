import serial
from Adafruit_IO import Client, Feed, RequestError
import re
import time



ADAFRUIT_IO_USERNAME = "Alexcoles"
ADAFRUIT_IO_KEY = "aio_rAAU81cu8zmKt5jYIgEvK0n5vCFg"

SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 115200

# Set up Adafruit IO client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Create a feed
# try:
#     feed = aio.feeds('test')
# except RequestError:  
#     feed = Feed(name='test')
#     feed = aio.create_feed(feed)

# Read data from the serial port and send it to Adafruit IO
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()  # read a line from the serial port
        # Get the numbers in the string
        numbers = re.findall(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?', data)
        # The first number is the temperature
        temp = float(numbers[0][0])
        # The second number is the pressure
        pressure = float(numbers[1][0])

        # The third number is the humidity
        humidity = float(numbers[2][0])

        aio.send('temptest', temp)
        time.sleep(3.0)
        aio.send('pressure-test', pressure)
        time.sleep(3.0)
        aio.send('humidity-test', humidity)
        # aio.send_data(feed.key, data)  # send the data to Adafruit IO
