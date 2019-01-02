# Changelog
All notable changes to this project will be documented in this file.

## [0.4.0] - 2019-01-02
### Added
- Added RepeatingArea.areas.contain() method

### Changed
- RepeatingArea.areas now returns a list-like object instead of a list
- Page.navigate() returns the Page instance

### Fixed
- If a Field is found multiple times, ensure an error is thrown when Field.find() is used

## [0.3.0] - 2018-11-06
### Added
- Appium compatibility started

### Changed
- RepeatingArea can now use any Field as a root
- Root Field no longer overrides Field.find()

## [0.2.3] - 2018-10-19
### Fixed
- Preserve class name on Fields that implement a performer
- Fix implementation of is_visible and is_not_visible when using Splinter

## [0.2.2] - 2018-10-16
### Added
- python 3.7 now supported
- stere.ini config file can be used to specify automation library
- Field implements the \__repr__ method
- RepeatingArea implements the \__len__ method

### Changed
- Splinter specific implementation refactored in Field.find()

## [0.2.1] - 2018-09-12
### Added
- Area.perform() can now take keyword arguments

## [0.2.0] - 2018-08-23
### Added
- Page class is now a Context Manager
- Added is_visible and is_not_visible methods to Field
- Added CHANGELOG file
