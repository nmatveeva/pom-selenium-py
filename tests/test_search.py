"""
These tests cover Bing searches.
"""

from pages.search import BingSearchPage
from pages.result import BingSearchResultPage


def test_basic_bing_search(browser):
    search_page = BingSearchPage(browser)
    result_page = BingSearchResultPage(browser)
    PHRASE = "page object model"

    # Given the Bing home page is displayed
    search_page.load()

    # When the user searches for phrase
    search_page.search(PHRASE)

    # Then the search result query is equal to phrase
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to phrase
    titles = result_page.result_link_titles()
    matches = [title for title in titles if PHRASE.lower() in title.lower()]
    assert len(matches) > 0

    # And the search result title contains phrase
    assert PHRASE in result_page.title()
