import time
import board
from adafruit_character_lcd.character_lcd_i2c import Character_LCD_I2C

def initialize_display():
    print(board.board_id)
    i2c = board.I2C()
    lcd = Character_LCD_I2C(i2c, 16, 2, address=0x27)
    lcd.clear()
    return lcd

def lprint(lcd, message):
    print(message)
    lcd.message = message

def timed_print(lcd, messages, delay=1):
    for message in messages:
        lprint(lcd, message)
        time.sleep(delay)
    lcd.clear()

def main():
    lcd = initialize_display()
    messages = ["Hello World!", "This is", "a test"]
    timed_print(lcd, messages)

if __name__ == "__main__":
    main()