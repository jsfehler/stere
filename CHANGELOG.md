# Changelog
All notable changes to this project will be documented in this file.

## [0.30.0] - 2021-09-13
### Added
- Area.text_to_dict() and Repeating.text_to_dict() methods.

## [0.29.0] - 2021-08-27
### Added
- Type hints are now exposed by the package.

## [0.28.0] - 2021-05-25
### Added
- Fields can now register and emit events.
- Fields emit 'before' and 'after' events when performer methods are called.

## [0.27.0] - 2021-05-19
### Added
- Splinter Input Field now has a highlight() method.

## [0.26.2] - 2021-05-18
### Fixed
- If XHRSpy.add() is called multiple times on the same page, the active and total counters are no longer reset.

## [0.26.1] - 2021-05-12
### Fixed
- If XHRSpy.add() is called multiple times on the same page, the hook is only added once.

## [0.26.0] - 2021-03-22
### Added
- Network spies to assist with navigating async web apps.

## [0.25.0] - 2021-02-24
### Added
- Repeating.has_children() now takes argument for minimum number of children that should exist.

## [0.24.0] - 2021-02-10
### Added
- Support for shadow DOM in the form of the ShadowRoot Field.

## [0.23.0] - 2021-01-18
### Fixed
- Nesting Repeating, Area, and RepeatingArea now correctly assigns root.

## [0.22.0] - 2021-01-13
### Changed
- Bumped minimum version of py-moneyed to 1.0.
- 'items' as a keyword is now allowed in Area and RepeatingArea.
- Missing root keyword in RepeatingArea now throws TypeError instead of ValueError.

### Fixed
- Area with no root inside a RepeatingArea should now work correctly.
- Area with no root inside a Repeating should now work correctly.


## [0.21.0] - 2020-12-08
### Changed
-  Repeating and RepeatingArea can now be placed inside an Area.

## [0.20.0] - 2020-09-25
### Changed
-  Stere.retry_time is used when searching for an attribute inside an element.
-  Nicer error message is thrown when an element is not found while doing an attribute lookup.

## [0.19.0] - 2020-09-22
### Changed
-  is_visible / is_not_visible methods try to handle stale element exceptions by retrying search.

## [0.18.0] - 2020-09-14
### Changed
-  Button and Link Fields wait for visible/clickable status before clicking.


## [0.17.0] - 2020-09-02
### Fixed
- Fields inside an Area with a root now pass wait_time to the root Field.


## [0.16.0] - 2020-04-20
### Changed
- Field.value_contains and Field.value_equals use Stere.retry_time as a default value.
- Splinter Dropdown.select() retries if value is not found.


## [0.15.0] - 2019-12-15
### Changed
- Speed up is_not_<x> methods. Requires splinter >=0.13.0.

## [0.14.0] - 2019-11-19
### Fixed
- Repeating.has_children no longer fails if no children found.
- Repeating.has_children no longer builds a list of children containers, just checks roots.

## [0.13.0] - 2019-11-16
### Added
- Field.is_<x> and Field.is_not_<x> methods now use Stere.retry_time if not specified.
- Stere.retry_time can be set through the stere.ini file.
- Repeating and RepeatingArea now have the has_children() method.

### Changed
- FindByDataStarAttribute renamed to FindByAttribute.

### Fixed
- Field.is_present() and Field.is_not_present() now work correctly with FindByAttribute.

## [0.12.0] - 2019-10-21
### Fixed
- Field.is_present() and Field.is_not_present() now work with Fields inside a RepeatingArea.

## [0.11.0] - 2019-10-17
### Added
- Page.page_url now built from Stere.base_url and Page.url_suffix.

## [0.10.0] - 2019-10-09
### Changed
- An Area can now be placed inside a RepeatingArea.
- Areas.containing now accepts nested values.
- Areas.contain now accepts nested values.

## [0.9.0] - 2019-09-12
### Added
- .is_clickable() and .is_not_clickable() are now available for splinter Fields.

## [0.8.0] - 2019-05-30
### Added
- Added Money Field in Splinter integration. [py-moneyed](https://github.com/limist/py-moneyed) is used to provide functionality.

## [0.7.0] - 2019-03-14
### Added
- Splinter and Appium Input Fields can now take a default_value parameter.
- Stere.url_navigator has a default value when Splinter is used.

### Changed
- If an invalid locator strategy is used, the error message now reports valid strategies.

## [0.6.1] - 2019-02-22
### Changed
- Base Field, Root, and Text now use @stere_performer instead of a custom perform method.

### Fixed
- Implicit Field calls now work with all Fields.

## [0.6.0] - 2019-02-22
### Added
- Field can take the keyword argument "returns". The object given will be returned after Field.perform() is called.
- Field now executes Field.perform() when called.

### Changed
- Stere decorators can now be used by importing Field.decorators.

## [0.5.0] - 2019-01-15
### Added
- Add Field.value_equals() and Field.value_contains() methods.
- Add Areas.containing().
- Add Repeating class to handle ridiculously nested collections.

### Changed
- Deprecated RepeatingArea.area_with().
- Areas container only accepts Area objects inside it.

### Fixed
- FindByDataStarAttribute inherits from SplinterBase.

## [0.4.0] - 2019-01-02
### Added
- Added RepeatingArea.areas.contain() method.

### Changed
- RepeatingArea.areas now returns a list-like object instead of a list.
- Page.navigate() returns the Page instance.

### Fixed
- If a Field is found multiple times, ensure an error is thrown when Field.find() is used.

## [0.3.0] - 2018-11-06
### Added
- Appium compatibility started.

### Changed
- RepeatingArea can now use any Field as a root.
- Root Field no longer overrides Field.find().

## [0.2.3] - 2018-10-19
### Fixed
- Preserve class name on Fields that implement a performer.
- Fix implementation of is_visible and is_not_visible when using Splinter.

## [0.2.2] - 2018-10-16
### Added
- python 3.7 now supported.
- stere.ini config file can be used to specify automation library.
- Field implements the \__repr__ method.
- RepeatingArea implements the \__len__ method.

### Changed
- Splinter specific implementation refactored in Field.find().

## [0.2.1] - 2018-09-12
### Added
- Area.perform() can now take keyword arguments.

## [0.2.0] - 2018-08-23
### Added
- Page class is now a Context Manager.
- Added is_visible and is_not_visible methods to Field.
- Added CHANGELOG file.
