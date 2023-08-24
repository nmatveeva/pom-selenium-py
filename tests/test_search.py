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


@pytest.mark.parametrize('img_id', [2, 7])
def test_sample_img_bing_search(browser, img_id):
    search_page = BingSearchPage(browser)
    result_page = BingSearchResultPage(browser)

    # Given the Bing home page is displayed
    search_page.load()

    # When the user opens Visual Search options
    search_page.open_img_search()

    # Then the search page displays Visual search options
    assert search_page.img_opts_is_displayed()

    # And the search page displays 8 sample images
    assert search_page.smpl_img_list_len() == 8

    # When the user searches for a sample image
    smpl_img_link = search_page.search_sample_img(img_id)

    # Then the search result page contains tabs
    tabs_matches = list(set(BingSearchResultPage.SEARCH_IMG_TABS_LIST) & set(result_page.result_tab_titles()))
    assert len(tabs_matches) > 0

    # And the main image section is displayed
    assert result_page.main_img_is_displayed()

    # And the close img search button is displayed
    assert result_page.close_img_btn_is_displayed()

    # And the search result title contains sample img link
    assert f"imgurl:{smpl_img_link} - Bing" == result_page.title()

    # And the search result query has a smpl img link
    assert f"imgurl:{smpl_img_link}" == result_page.search_input_value()
