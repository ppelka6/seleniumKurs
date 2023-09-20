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
driver.get("C:/Users/48730/Downloads/Test.html")
# driver.set_window_size(100, 100)
driver.maximize_window()
time.sleep(1)
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "newPage"))

wartosc = "Bartek"
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc +"')", driver.find_element(By.ID, "fname"))
time.sleep(1)

driver.quit()