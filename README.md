# adafruit_ft232h

This repository contains Python scripts for interacting with the Adafruit FT232H breakout board on Linux systems.

## Main Tool: `drivelightsft232h.py`

A tool to monitor Linux filesystem activity (using `fanotify`) and flash LEDs connected to an FT232H board. It provides a visual indication of read and write operations on a specified mount point.

### Requirements

-   **Root Privileges:** Required for `fanotify` access.
-   **Hardware:** Adafruit FT232H USB to GPIO/SPI/I2C Breakout.
-   **Software:**
    -   Python 3.6+
    -   `adafruit-blinka` library
    -   Linux Kernel with `fanotify` support (most modern distributions)

### Setup

1.  **Install dependencies:**
    ```bash
    pip install adafruit-blinka
    ```

2.  **Configure FT232H udev rules:**
    To use the FT232H without root privileges (for GPIO, I2C, SPI), add the following rule to `/etc/udev/rules.d/99-ftdi.rules`:
    ```udev
    SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6014", GROUP="plugdev", MODE="0666"
    ```
    Then reload the rules:
    ```bash
    sudo udevadm control --reload-rules && sudo udevadm trigger
    ```
    *Note: `drivelightsft232h.py` still requires `sudo` for `fanotify` access.*

### Usage

The script must be run with `sudo` because of the `fanotify` requirement.

```bash
sudo python drivelightsft232h.py --mount / --read C0 --write C1
```

**Arguments:**
-   `--mount`: The mount point to monitor (default: `/`).
-   `--read`: The FT232H pin to flash for read operations (default: `C0`).
-   `--write`: The FT232H pin to flash for write operations (default: `C1`).

## Other Included Scripts

-   `blink.py`: Simple LED blinking test for pin `C0`.
-   `test_ft232h.py`: Scans the I2C bus to verify the FT232H is connected and working.
-   `randon_blinker_2_leds.py`: Randomly blinks LEDs on pins `C0` through `C7`.
-   `wander.py` and `display.py`: Additional example/testing scripts.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
