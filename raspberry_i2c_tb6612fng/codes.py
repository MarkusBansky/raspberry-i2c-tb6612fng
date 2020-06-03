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

from enum import Enum


class TB6612FNGCodes(Enum):
    """
    Operational codes used to send commands to the driver module via I2C interface.
    """

    # module address
    GMD_I2C_ADDRESS: int = 0x14

    # commands for modules
    GMD_CMD_BRAKE: int = 0x00
    GMD_CMD_STOP: int = 0x01
    GMD_CMD_CW: int = 0x02
    GMD_CMD_CCW: int = 0x03
    GMD_CMD_STANDBY: int = 0x04
    GMD_CMD_NOT_STANDBY: int = 0x05
    GMD_CMD_STEPPER_RUN: int = 0x06
    GMD_CMD_STEPPER_STOP: int = 0x07
    GMD_CMD_STEPPER_KEEP_RUN: int = 0x08
    GMD_CMD_SET_ADDR: int = 0x11
