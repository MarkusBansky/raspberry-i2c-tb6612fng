# RaspberryPi Grove TB6612FNG Motor Shield Library

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/raspberry-i2c-tb6612fng.svg)](https://pypi.python.org/pypi/raspberry-i2c-tb6612fng/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/raspberry-i2c-tb6612fng.svg)](https://pypi.python.org/pypi/raspberry-i2c-tb6612fng/)

This is an open source port of the official Grove Motor Shield TB6612FNG library for Arduino to Python for Raspberry Pi.

## Features
  - Library aims to be identical to the [Grove Arduino LIbrary](https://github.com/Seeed-Studio/Grove_Motor_Driver_TB6612FNG) for ease of use
  - Control [Grove I2C Motor Driver on TB6612FNG](https://wiki.seeedstudio.com/Grove-I2C_Motor_Driver-TB6612FNG/)
  - **(Experimental)** Includes 6 easing functions for smooth start of the motors, limited to a single motor at once

## Requirements
  - RaspberryPi I2C enabled
  - Python 3.13 or higher

> [!NOTE] This library was tested in 2025 on Raspberry Pi 5 8GB with Raspberry Pi OS (64-bit Debian 1:6.12.47-1+rpt1 2025-09-16) with kernel version 6.12 running Python 3.13.5 and library version 0.3.0.

# Getting started

## 1. Enable I2C on your Raspberry Pi

If you have not done so already, you will need to enable I2C on your Raspberry Pi. You can do this by running `sudo raspi-config` in your terminal, then navigating to `Interfacing Options` -> `I2C` and enabling it. After that, you may need to reboot your Raspberry Pi.

## 2. Install Python

You can install the latest version of python on your Raspberry Pi by running the following commands in your terminal:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

It is recommended to use a virtual environment for your python projects. You can create one by running the following commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install the library

Install this library:

```bash
python3 -m pip install raspberry-i2c-tb6612fng
```

## 4. Example usage

```python
import time

from raspberry_i2c_tb6612fng import MotorDriverTB6612FNG, TB6612FNGMotors

# create an instance of the driver, connected to i2c
driver = MotorDriverTB6612FNG()

# drive both motors forward
driver.dc_motor_run(TB6612FNGMotors.MOTOR_CHA, 200)
driver.dc_motor_run(TB6612FNGMotors.MOTOR_CHB, 200)

# pause for a second
time.sleep(1)

# stop the motors
driver.dc_motor_break(TB6612FNGMotors.MOTOR_CHA)
driver.dc_motor_break(TB6612FNGMotors.MOTOR_CHB)
```

# License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.