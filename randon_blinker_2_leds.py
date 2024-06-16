import random

import board
import digitalio
import time

random.seed()

leds=[
    digitalio.DigitalInOut(board.C0),
    digitalio.DigitalInOut(board.C1),
    digitalio.DigitalInOut(board.C2),
    digitalio.DigitalInOut(board.C3),
    digitalio.DigitalInOut(board.C4),
    digitalio.DigitalInOut(board.C5),
    digitalio.DigitalInOut(board.C6),
    digitalio.DigitalInOut(board.C7),
    ]
for led in leds:
    led.direction=digitalio.Direction.OUTPUT
    led.value=0


while True:
    if random.randint(0, 10000) == random.randint(0, 10000):
        led = random.choice(leds)
        led.value=not led.value
        #print(f'\r{led._pin.id}', end='', flush=True)
        time.sleep(0.0)
