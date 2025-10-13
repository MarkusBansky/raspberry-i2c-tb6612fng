# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - 2025-10-13

### Added
- Configurable I2C bus parameter in `MotorDriverTB6612FNG` constructor (defaults to bus 1)
- Support for Python 3.13

### Changed
- Updated README with comprehensive getting started guide including I2C setup and Python installation instructions
- Modernized README with clearer structure and sections
- Improved documentation with installation via virtual environment
- Updated minimum Python version requirement from 3.6 to 3.13
- Code formatting improvements across all modules (consistent style, better readability)
- Simplified package description in setup.py

### Removed
- IDE configuration files (.idea directory) now properly ignored
- Removed PyPI license and Codacy badges from README
- Removed outdated documentation references

### Infrastructure
- Added .vscode/ and .idea/ to .gitignore for better IDE file management
