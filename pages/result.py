"""
This module contains BingSearchResultPage,
the page object for the Bing search result page.
"""

from selenium.webdriver.common.by import By


class BingSearchResultPage:

    RESULT_LINKS = (By.XPATH, '//div/h2/a')
    SEARCH_INPUT = (By.ID, 'sb_form_q')
    SEARCH_IMG_TABS = (By.CSS_SELECTOR, 'li[role="tab"]')
    SEARCH_MAIN_IMG = (By.ID, 'mainImageRegion')
    SEARCH_IMG_CLOSE_BTN = (By.CSS_SELECTOR, 'div[class="close nofocus"]')
    SEARCH_IMG_TABS_LIST = ["All", "Pages with this image", "Shop for similar", "Related content"]

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

    def result_tab_titles(self) -> list:
        tabs = self.browser.find_elements(*self.SEARCH_IMG_TABS)
        titles = [tab.text for tab in tabs]
        return titles

    def main_img_is_displayed(self):
        main_img = self.browser.find_element(*self.SEARCH_MAIN_IMG)
        return main_img.is_displayed()

    def close_img_btn_is_displayed(self):
        close_img = self.browser.find_element(*self.SEARCH_IMG_CLOSE_BTN)
        return close_img.is_displayed()
