import configparser
import os


def _parse_config():
    parser = configparser.ConfigParser()
    cwd = os.getcwd()
    file_path = f'{cwd}/stere.ini'
    parser.read(file_path)
    return parser


class BrowserEnabled:
    """Base class that stores attributes at the class level,
    shared by every object that inherits from this class.

    Attributes:
        browser (object): Pointer to what is driving the automation.
        url_navigation (str): Name of the function that opens a page.
        library (str): Name of the automation library to use. Default is
            splinter.
    """
    browser = None
    url_navigator = ''
    library = 'splinter'

    parser = _parse_config()
    if parser.has_section('stere'):
        if parser.has_option('stere', 'library'):
            library = parser.get('stere', 'library')
