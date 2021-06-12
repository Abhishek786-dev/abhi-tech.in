from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://18.117.179.23/abhi-tech.in/')
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys("abhishek@gmail.com")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
