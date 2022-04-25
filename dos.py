'''
Elabore un programa que encienda la mitad de los leds, durante 1 segundo y la mitad de leds durante 2 segundos 
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

print("Let's to turn on the half of the leds")
turn_first_half(_board, 1, False)
time.sleep(1)
turn_first_half(_board, 0, False)

turn_second_half(_board, 1, False)
time.sleep(2)
turn_second_half(_board, 0, False)




