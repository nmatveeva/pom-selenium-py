"""
This module contains shared fixtures
"""

import pytest
import selenium.webdriver
import json
import os
from datetime import datetime as dt

from constants import BASE_DIR


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config) -> None:
    if not os.path.exists(f'{BASE_DIR + "reports"}'):
        os.makedirs(f'{BASE_DIR}/reports')
    config.option.htmlpath = (f'{BASE_DIR}reports/'
                              + dt.now().strftime('%Y-%m-%d_%H-%M-%S',)
                              + '_report.html')


@pytest.fixture(scope='session')
def config():

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Chrome', 'Headless Chrome', 'Firefox']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config


@pytest.fixture()
def browser(config):

    # Init the Webdriver instance
    if config['browser'] == 'Chrome':
        br = selenium.webdriver.Chrome()
    elif config['browser'] == 'Firefox':
        br = selenium.webdriver.Firefox()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        br = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    br.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield br

    # Quit the WebDriver instance for the cleanup
    br.quit()
