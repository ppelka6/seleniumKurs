from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

op = Options()
op.add_experimental_option("detach", True)
op.add_argument("--disable-dev-shm-usage")
op.add_argument("--disable-gpu")
op.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=op)
driver.get("C:/Users/48730/Downloads/iFrameTest%20(1).html")
# driver.set_window_size(100, 100)
driver.maximize_window()
time.sleep(1)

print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h1").text)


driver.quit()