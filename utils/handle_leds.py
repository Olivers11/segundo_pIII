import time

def turn_ascend(_board, mode):
    for i in range(10, 14):
        _board.digital[i].write(mode)
        time.sleep(0.2)
    time.sleep(0.8)



def turn_off_all(_board):
    for i in range(10, 14):
        _board.digital[i].write(0)

    time.sleep(0.8)



def turn_descend(_board, mode):
    for i in range(13, 9, -1):
        _board.digital[i].write(mode)
        time.sleep(0.2)
    time.sleep(0.8)

def turn_first_half(_board, mode, sl):
    _board.digital[10].write(mode)
    _board.digital[11].write(mode)
    if sl: time.sleep(0.8);


def turn_second_half(_board, mode, sl):
    _board.digital[12].write(mode)
    _board.digital[13].write(mode)
    if sl: time.sleep(0.8);


def turn_led(pin, mode):
    import pyfirmata
    PORT="/dev/ttyUSB0"
    _board = pyfirmata.Arduino(PORT)
    _board.digital[pin].write(mode)





