import unittest
from selenium import WebdriverWait
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("www.python.org")

    def test_search_in_python(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.main_page(self.driver)
        #Checks if the word "Python" is in the title
        assert main_page.is_title_matches(), "Python.org title doesnt match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.search_results_page(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
