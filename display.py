import time
import board
from adafruit_character_lcd.character_lcd_i2c import Character_LCD_I2C

def lprint(lcd, message):
    print(message)
    lcd.message = message

print(board.board_id)
i2c = board.I2C()  # uses board.SCL and board.SDA
lcd = Character_LCD_I2C(i2c, 16, 2, address=0x27)
lcd.clear()
lprint(lcd, "Hello World!")
#time.sleep(1)
lprint(lcd, "This is")
#time.sleep(1)
lprint(lcd, "a test")
#time.sleep(1)
lcd.clear()