# Changelog
All notable changes to this project will be documented in this file.


## [0.9.0] - 2019-09-12
### Added
- .is_clickable() and .is_not_clickable() are now available for splinter Fields.

## [0.8.0] - 2019-05-30
### Added
- Added Money Field in Splinter integration. [py-moneyed](https://github.com/limist/py-moneyed) is used to provide functionality.

## [0.7.0] - 2019-03-14
### Added
- Splinter and Appium Input Fields can now take a default_value parameter
- Stere.url_navigator has a default value when Splinter is used

### Changed
- If an invalid locator strategy is used, the error message now reports valid strategies

## [0.6.1] - 2019-02-22
### Changed
- Base Field, Root, and Text now use @stere_performer instead of a custom perform method

### Fixed
- Implicit Field calls now work with all Fields

## [0.6.0] - 2019-02-22
### Added
- Field can take the keyword argument "returns". The object given will be returned after Field.perform() is called
- Field now executes Field.perform() when called

### Changed
- Stere decorators can now be used by importing Field.decorators

## [0.5.0] - 2019-01-15
### Added
- Add Field.value_equals() and Field.value_contains() methods
- Add Areas.containing()
- Add Repeating class to handle ridiculously nested collections

### Changed
- Deprecated RepeatingArea.area_with()
- Areas container only accepts Area objects inside it

### Fixed
- FindByDataStarAttribute inherits from SplinterBase

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
