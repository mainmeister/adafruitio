import time
import board
import digitalio

def main():
    print(f"Board ID: {board.board_id}")
    if board.board_id == "GENERIC_LINUX_PC":
        print("Hint: If you are using an FT232H, make sure to set 'export BLINKA_FT232H=1' in your shell.")
        return

    # FT232H breakout boards usually don't have a user-controllable "built-in" LED.
    # We use Pin C0 (on the upper row of pins) as a default for blinking.
    # You can also change this to board.D7 (the pin labeled '7') if you prefer.
    led_pin = board.C0
    
    print(f"Blinking LED on pin {led_pin}...")
    
    led = digitalio.DigitalInOut(led_pin)
    led.direction = digitalio.Direction.OUTPUT

    try:
        while True:
            led.value = True
            print("LED ON")
            time.sleep(0.5)
            led.value = False
            print("LED OFF")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Blink stopped.")
    finally:
        led.deinit()

if __name__ == "__main__":
    main()
