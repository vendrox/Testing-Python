from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import chromedriver_binary 

def test_simple_load():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome("C:\\Users\\Usuario\\Testing-Python\\resources\\chromedriver", chrome_options=chrome_options)
	driver.get("https://egarciasec.github.io/pdex/")
	assert driver.find_element_by_xpath('//*[@id="root"]/h1')
	driver.quit()