"""
These tests cover Bing searches.
"""

import pytest
from pages.search import BingSearchPage
from pages.result import BingSearchResultPage


@pytest.mark.parametrize('phrase', ['page object model', 'selenium webdriver', 'python'])
def test_basic_bing_search(browser, phrase):
    search_page = BingSearchPage(browser)
    result_page = BingSearchResultPage(browser)

    # Given the Bing home page is displayed
    search_page.load()

    # When the user searches for phrase
    search_page.search(phrase)

    # Then the search result query is equal to phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to phrase
    titles = result_page.result_link_titles()
    matches = [title for title in titles if phrase.lower() in title.lower()]
    assert len(matches) > 0

    # And the search result title contains phrase
    assert phrase in result_page.title()
