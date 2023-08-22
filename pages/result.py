"""
This module contains BingSearchResultPage,
the page object for the Bing search result page.
"""

from selenium.webdriver.common.by import By


class BingSearchResultPage:

    RESULT_LINKS = (By.XPATH, '//div/h2/a')
    SEARCH_INPUT = (By.ID, 'sb_form_q')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title
