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

paragraf = driver.find_elements(By.TAG_NAME, "p")

if len(paragraf) > 0:
    print("Dany element istnieje na stronie")
else:
    print("Brak elementu na stronie")

try:
    driver.find_element(By.TAG_NAME, "pr")
except NoSuchElementException:
    print("Element nie isnieje")


driver.quit()