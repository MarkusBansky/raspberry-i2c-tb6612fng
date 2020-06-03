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

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='raspberry-i2c-tb6612fng',
    version='0.1.2',
    packages=find_packages(exclude=['tests*']),
    license='GNU General Public License',
    description='A port of Grove Motor Driver TB6612FNG library for python and RaspberryPI. '
                'This library also includes easing functions to control your motors with smooth transitions.'
                'Easing functions are available for dc motors only.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['smbus'],
    keywords='raspberry i2c tb6612fng grove motor',
    url='https://github.com/MarkusBansky/raspberry-i2c-tb6612fng',
    author='Markiian Benovskyi',
    author_email='admin@markiian-benovskyi.com',
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
    ],
)
