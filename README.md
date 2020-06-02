# RaspberryPi Grove TB6612FNG Motor Shield Library

This is a private open source port of the official Grove Motor Shield TB6612FNG library for Arduino to Python3 on RaspberryPI.

## Features
  - Library is identical to the official Grove
  - It depends only on built in libraries**

***library requires I2C to be activated on the RaspberryPI board running Linux build*

## Requirements
  - RaspberryPi linux image
  - Python 3.6+
  - **smbus** library
  - **time** library
  - **math** library

This library also includes a experimental python easing functions:
  - Contains 6 easing functions for smooth start of motors
  - Easing functions currently can only be used on a single motor at once
  - Containing IN and OUT functions


This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

# How to use
Basic usage of this library is very simple. First of all make sure you are running the latest released version of **pip**.

This library requires you to add an additional `index-url` to **pip.conf** in order to install it. You can do this by editing your config file with `sudo nano /etc/pip.conf` and inserting this line just after the `[global]` section:

```config
index-url=https://pypi.python.org/
```

Now you can install the package as usual, for python3 use something for example:
`python3 -m pip install raspberry-i2c-tb6612fng`

Next, after successfull instalation you can import this library and start using it in your project like this:

```python
# import default libraries that are used in this example
import time

# import the library
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

##### Documentation

If you would like to read about all functions available, please refer to this projects Wiki page on GitHub.