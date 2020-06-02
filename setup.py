from setuptools import setup, find_packages

setup(
    name='raspberry-i2c-tb6612fng',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='Creative Commons Attribution-ShareAlike 4.0 International Public License',
    description='A port of Grove Motor Driver TB6612FNG library for python and RaspberryPI. '
                'This library also includes easing functions to control your motors with smooth transitions.'
                'Easing functions are available for dc motors only.',
    long_description=open('README.md').read(),
    install_requires=['smbus','time','math'],
    url='https://github.com/MarkusBansky/raspberry-i2c-tb6612fng',
    author='Markiian Benovskyi',
    author_email='admin@markiian-benovskyi.com'
)
