#create window for eel
import eel
import sys
from led import *
sys.path.append("..")
eel.init("htmls")

@eel.expose
def process(pin, mode):
    turn_led(pin, mode)

eel.start("index.html", size=(400,400))

