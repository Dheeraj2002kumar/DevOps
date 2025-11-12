import unittest
import time 
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteTitle(unittest.TestCase):
    def setUp(self):
        """Setup browser before each test"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://concertcraze.netlify.app/")
        time.sleep(2)

    def test_title_verification(self):
        """Check if website title is correct"""
        driver = self.driver
        expected_title = "Landing Page"  # correct title
        actual_title = driver.title

        self.assertEqual(expected_title, actual_title)
        print(f"Test Passed: Title matches -> {actual_title}")

    def tearDown(self):
        """Close browser after test"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reports'   # report folder will be created automatically
        )
    )