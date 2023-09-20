from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

op = Options()
op.add_experimental_option("detach", True)
op.add_argument("--disable-dev-shm-usage")
op.add_argument("--disable-gpu")
op.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=op)
driver.get("file:///C:/Users/48730/Downloads/Waits2.html")
driver.maximize_window()
wait = WebDriverWait(driver,10, 0.5)
# driver.implicitly_wait(10)
driver.find_element(By.ID, "clickOnMe").click()
wait.until(lambda wd: len(wd.find_elements(By.TAG_NAME, "p")) ==1)
print(driver.find_element(By.TAG_NAME, "p").text)
driver.quit()