"""
This module contains BingSearchPage,
the page object for the Bing search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BingSearchPage:

    URL = "https://www.bing.com/"
    SEARCH_INPUT = (By.ID, 'sb_form_q')
    SEARCH_IMG_BTN = (By.ID, 'sb_sbip')
    SEARCH_IMG_OPTS = (By.ID, 'sb_sbiopc')
    SEARCH_PASTE_INPUT = (By.ID, 'sb_pastepn')
    SEARCH_TAKE_PIC_BTN = (By.ID, 'sb_tkpct')
    SMPL_IMG_LIST = (By.CSS_SELECTOR, 'img[class*="sbiDmImg"]')

    VISUAL_SEARCH_HEADER = "Try Visual Search"
    SAMPLE_IMG_TUTOR = "Click a sample image to try it"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def open_img_search(self):
        search_img_btn = self.browser.find_element(*self.SEARCH_IMG_BTN)
        search_img_btn.click()

    def img_opts_is_displayed(self):
        img_opts = self.browser.find_element(*self.SEARCH_IMG_OPTS)
        return img_opts.is_displayed()

    def smpl_img_list_len(self):
        smpl_img_list = self.browser.find_elements(*self.SMPL_IMG_LIST)
        return len(smpl_img_list)

    def search_sample_img(self, img_id: int) -> str:
        sample_img_id = f'.sbiDmImg:nth-child({img_id})'
        sample_img = self.browser.find_element(By.CSS_SELECTOR, sample_img_id)
        link = sample_img.get_attribute("sbi-hi-src")

        sample_img.click()

        return link
