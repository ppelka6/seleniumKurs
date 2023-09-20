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
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
# driver.set_window_size(100, 100)
driver.maximize_window()
time.sleep(1)

draggable = driver.find_element(By.ID, "draggable")
drop_targer = driver.find_element(By.ID, "droptarget")

webdriver.ActionChains(driver).drag_and_drop(draggable,drop_targer).perform()

driver.quit()