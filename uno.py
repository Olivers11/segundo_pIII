'''
Elabore un programa que desde python se enciendan secuencialmente todos los leds
de manera ascendente y descendente
'''

import pyfirmata
import time
from utils.handle_leds import *

_board = pyfirmata.Arduino('/dev/ttyUSB0')

#config pin 13 like output
it = pyfirmata.util.Iterator(_board)
it.start()
_board.digital[13].mode = pyfirmata.OUTPUT
_board.digital[12].mode = pyfirmata.OUTPUT
_board.digital[11].mode = pyfirmata.OUTPUT
_board.digital[10].mode = pyfirmata.OUTPUT

print("Let's to turn on all leds in 3 seconds")
time.sleep(3)
turn_ascend(_board, 1)
turn_off_all(_board)
turn_descend(_board, 1)













