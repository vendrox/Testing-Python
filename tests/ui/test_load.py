import pytest
import time
from selenium import webdriver
<<<<<<< HEAD
import chromedriver_binary 
=======
import chromedriver_binary # noqa F401
>>>>>>> 4e58feee10e7f04f33b0665a7be984763ea13daf
from core.MainPage.page import MainPage


@pytest.mark.ui
class TestLoad:

    name = "Bulbasaur"

    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
<<<<<<< HEAD
        chrome_options.add_argument("--headless")
=======
>>>>>>> 4e58feee10e7f04f33b0665a7be984763ea13daf
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("https://egarciasec.github.io/pdex/")

    def teardown(self):
        self.driver.quit()

    def test_simple_load(self):
        driver = self.driver
        MainPage(driver).assert_page_title()

    def test_pokemon_search(self):
        driver = self.driver
        MainPage(driver).search(self.name)
        for _ in range(0, 3):
            try:
                MainPage(driver).assert_expected_name("#1 Bulbasaur")
                break
            except Exception:
                time.sleep(1)

    def test_pokemon_image(self):
        driver = self.driver
        MainPage(driver).search(self.name)
        for _ in range(0, 3):
            try:
                MainPage(driver).assert_pokemon_image()
                break
            except Exception:
                time.sleep(1)
