from selenium import webdriver

class MainPage:

	search_input='//*[@id="PokeINFO"]/input'
	search_button='//*[@id="PokeINFO"]/button'
	search_image='//*[@id="root"]/h2'

	def __init__(self, driver):
		self.driver=driver

	def search(self, name):
		input_element = self.driver.find_element_by_xpath(self.search_input)
		input_element.clear()
		input_element.send_keys(name)
		search = self.driver.find_element_by_xpath(self.search_button)
		search.click()