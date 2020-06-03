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


class TB6612FNGStepper(Enum):
    """
    An enum for stepper motor commands enum.
    """

    FULL_STEP: int = 0
    WAVE_DRIVE: int = 1
    HALF_STEP: int = 2
    MICRO_STEPPING: int = 3
