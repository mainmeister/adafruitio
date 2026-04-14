import board
import busio

print(f"Board ID: {board.board_id}")
try:
    i2c = board.I2C()
    print("I2C Bus object created successfully.")
    
    while not i2c.try_lock():
        pass
    try:
        addresses = i2c.scan()
        print(f"I2C addresses found: {[hex(device_address) for device_address in addresses]}")
        if not addresses:
            print("No I2C devices found. Check wiring and if D1/D2 are jumpered together.")
    finally:
        i2c.unlock()
except Exception as e:
    print(f"Failed to initialize I2C: {e}")
    if board.board_id == "GENERIC_LINUX_PC":
        print("Hint: If you are using an FT232H, remember to set 'export BLINKA_FT232H=1' in your shell.")
