from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

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

element = driver.find_element(By.XPATH, "//input[@type='checkbox']")
element.click()
time.sleep(1)

if element.is_selected():
    print("Wartość jest zaznaczona, trzeba odznaczyć")
    element.click()
else:
    print("Nie jest zaznaczony , więc zaznacze")
    element.click()

driver.quit()

