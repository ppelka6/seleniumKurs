from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

op = Options()
op.add_experimental_option("detach", True)
op.add_argument("--disable-dev-shm-usage")
op.add_argument("--disable-gpu")
op.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=op)
driver.get("file:///C:/Users/48730/Downloads/FileUpload.html")
# driver.set_window_size(100, 100)
driver.maximize_window()
time.sleep(1)

upload_input = driver.find_element(By.ID, "myFile")

path = os.path.abspath("upload.txt")
driver.save_screenshot("screenshots/before_upload.png")
upload_input.send_keys(path)
time.sleep(1)

driver.save_screenshot("screenshots/after_upload.png")

driver.quit()