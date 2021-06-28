import os

import requests
from requests.auth import HTTPBasicAuth


APP_URL = (
    'https://github.com/jsfehler/stere_ios_test_app/'
    'raw/master/build/stere_ios_test_app.zip'
)
APP_FILENAME = 'stere_ios_test_app.zip'

SAUCE_UPLOAD_URL = 'https://api.us-west-1.saucelabs.com/v1/storage/upload'
SAUCE_HEADERS = {
    'Content-Type': 'application/octet-stream',
}
SAUCE_USERNAME = os.getenv('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.getenv('SAUCE_ACCESS_KEY')


def get_app():
    """Download the test app and save it to disk."""
    response = requests.get(APP_URL)

    with open(APP_FILENAME, 'wb') as f:
        for block in response.iter_content():
            f.write(block)


def upload_app_to_sauce():
    """Upload the test app to sauce labs."""
    with open(APP_FILENAME, 'rb') as f:
        data = f.read()

    requests.post(
        SAUCE_UPLOAD_URL,
        headers=SAUCE_HEADERS,
        data=data,
        auth=HTTPBasicAuth(SAUCE_USERNAME, SAUCE_ACCESS_KEY),
    )


if __name__ == '__main__':
    # Upload the IOS test app to sauce storage before running any tests.
    get_app()
    upload_app_to_sauce()
