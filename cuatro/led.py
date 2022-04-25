import pyfirmata
PORT="/dev/ttyUSB0"
_board = pyfirmata.Arduino(PORT)

def turn_led(pin, mode):
    _board.digital[pin].write(mode)


