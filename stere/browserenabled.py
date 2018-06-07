class BrowserEnabled:
    """Base class that stores attributes at the class level,
    shared by every object that inherits from this class.

    Arguments:
        browser (object): Pointer to what is driving the automation.
        url_navigation (str): Name of the function that opens a page.
    """
    browser = None
    url_navigator = ''
