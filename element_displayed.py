from selenium import webdriver
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

paragraf = driver.find_element(By.TAG_NAME, "p")

if paragraf.is_displayed():
    print("Is displayed")
    print(paragraf.text)
else:
    print("Is not displayed")
    print(paragraf.get_attribute("textContent"))

driver.quit()





driver.quit()
