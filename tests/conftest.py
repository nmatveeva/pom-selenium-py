"""
This module contains shared fixtures
"""

import pytest
import selenium.webdriver
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


@pytest.fixture()
def browser():
    br = selenium.webdriver.Chrome()
    br.implicitly_wait(5)
    yield br
    br.quit()
