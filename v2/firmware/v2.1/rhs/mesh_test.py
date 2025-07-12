from sx1262 import SX1262
import time
import board
import busio
import digitalio
import time
from analogio import AnalogIn
import terminalio
import displayio
import adafruit_gps

######## Display setup

from adafruit_display_text import label
import adafruit_displayio_ssd1306

try:
    from i2cdisplaybus import I2CDisplayBus
except ImportError:
    from displayio import I2CDisplay as I2CDisplayBus
    
displayio.release_displays()
i2c = busio.I2C(board.P0_11, board.P1_04)
#i2c = board.I2C()
display_bus = I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()
display.root_group = splash

text="startup ..."

ta = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=5, y=20)
splash.append(ta)

uart_mesh = busio.UART(board.P0_06, board.P0_08, baudrate=9600, timeout=0)

sendstring="hello world!"

uart_mesh.write(bytes(sendstring, "ascii"))

ta.text="sent!"

while True:

    data = uart_mesh.read(32)
    if data is not None:
        data_string = ''.join([chr(b) for b in data])
        print("len:",len(data))




