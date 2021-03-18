import configparser
import os
import typing


def _parse_config() -> configparser.ConfigParser:
    parser = configparser.ConfigParser()
    cwd = os.getcwd()
    file_path = f'{cwd}/stere.ini'
    parser.read(file_path)
    return parser


def _get_config_option(
    parser: configparser.ConfigParser,
    section: str = 'stere',
    option: str = '',
    default: typing.Optional[typing.Any] = '',
) -> typing.Any:
    """Get an option from a config section, if it exists.

    Arguments:
        section(str): The name of the section
        option(str): The name of the option

    Returns:
        str: The found value, or else the default value

    """
    if parser.has_option(section, option):
        return parser.get(section, option)
    return default


class BrowserEnabled:
    """Base class that stores attributes at the class level,
    shared by every object that inherits from this class.

    If a stere.ini file is found, the attributes will be set from there.

    Attributes:
        browser (object): Pointer to what is driving the automation.
        base_url (str): Used as the url when navigating to pages.
        url_suffix (str): Appended to base_url when navigating to pages.
        retry_time (int): The maximum amount of time in seconds to try and
            find an element on a page.
        library (str): Name of the automation library to use. Default is
            splinter.
        url_navigator (str): Name of the function that opens a page.

    """

    browser = None
    base_url: str = ''
    url_suffix: str = ''
    retry_time: int = 5

    xhr_spy_sleep_time = 1
    fetch_spy_sleep_time = 1

    # Default values for automation libraries
    library_defaults = {
        'splinter': {
            'url_navigator': 'visit',
        },
    }

    library: str = 'splinter'
    url_navigator: str = library_defaults[library]['url_navigator']

    # If a config file exists, get settings from there.
    parser = _parse_config()
    if parser.has_section('stere'):
        library = _get_config_option(parser, option='library', default=library)
        url_navigator = _get_config_option(
            parser, option='url_navigator', default=url_navigator,
        )
        base_url = _get_config_option(
            parser, option='base_url', default=base_url,
        )
        url_suffix = _get_config_option(
            parser, option='url_suffix', default=url_suffix,
        )
        retry_time = _get_config_option(
            parser, option='retry_time', default=retry_time,
        )
