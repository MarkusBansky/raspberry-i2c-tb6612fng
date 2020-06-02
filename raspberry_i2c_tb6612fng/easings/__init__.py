#
#      Copyright (C) 2020  Markiian Benovskyi
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import time
import math


def tb6612fng_easy_fn_in_expo(t):
    """
    Exponential easing function.
    :param t: Time from 0 to 1 where 1 is the end of transition.
    :return: A X value for this transition from 0 to 1.
    """
    return 0 if t == 0 else pow(2, 10 * t - 10)


def tb6612fng_easy_fn_out_expo(t):
    """
    Exponential easing function.
    :param t: Time from 0 to 1 where 1 is the end of transition.
    :return: A X value for this transition from 0 to 1.
    """
    return 1 if t == 1 else 1 - pow(2, -10 * t)


def tb6612fng_easy_fn_in_quad(t):
    """
    Square easing function.
    :param t: Time from 0 to 1 where 1 is the end of transition.
    :return: A X value for this transition from 0 to 1.
    """
    return t * t


def tb6612fng_easy_fn_out_quad(t):
    """
    Square out easing function.
    :param t: Time from 0 to 1 where 1 is the end of transition.
    :return: A X value for this transition from 0 to 1.
    """
    return 1 - (1 - t) * (1 - t)


def tb6612fng_easy_fn_in_cubic(t):
    """
    Cubic easing function.
    :param t: Time from 0 to 1 where 1 is the end of transition.
    :return: A X value for this transition from 0 to 1.
    """
    return t * t * t


def tb6612fng_easy_fn_out_cubic(t):
    """
    Cubic out easing function.
    :param t: Time from 0 to 1 where 1 is the end of transition.
    :return: A X value for this transition from 0 to 1.
    """
    return 1 - math.pow(1 - t, 3)


def tb6612fng_easy(driver_inst, motor, speed_from, speed_to, fn, transition_time=3, transition_step=0.1):
    """
    This function creates a smooth transition from starting speed to target in specific amount of seconds.
    :param driver_inst: A TB6612FNG I2C driver class instance.
    :param motor: Selection which motor to run. MOTOR_CHA or MOTOR_CHB.
    :param speed_from: The starting speed of the motor to make transition from.
    :param speed_to: The target speed of motor.
    :param fn: An easing function.
    :param transition_time: Time to make this transition in seconds. (max 5 sec). Default: 3sec.
    :param transition_step: Time increase step. (max 0.25sec) Default: 100 ms.
    :return: nothing
    """
    if transition_time > 5:
        transition_time = 5
    elif transition_time <= 0.1:
        transition_time = 0.1

    if speed_from < 25:
        speed_from = 25

    if transition_step > 0.25:
        transition_step = 0.25
    elif transition_step < 0.01:
        transition_step = 0.01

    elapsed = transition_time

    while elapsed > 0:
        t = (transition_time - elapsed) / transition_time
        y = fn(t)

        diff = (speed_to - speed_from) * y

        driver_inst.dc_motor_run(motor, speed_from + diff)

        elapsed -= transition_step
        time.sleep(transition_step)
