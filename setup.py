from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='raspberry-i2c-tb6612fng',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='Creative Commons Attribution-ShareAlike 4.0 International Public License',
    description='A port of Grove Motor Driver TB6612FNG library for python and RaspberryPI. '
                'This library also includes easing functions to control your motors with smooth transitions.'
                'Easing functions are available for dc motors only.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['smbus', 'time', 'math'],
    keywords='raspberry i2c tb6612fng grove',
    url='https://github.com/MarkusBansky/raspberry-i2c-tb6612fng',
    author='Markiian Benovskyi',
    author_email='admin@markiian-benovskyi.com',
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Creative Commons License",
        "Operating System :: Linux",
    ],
)
