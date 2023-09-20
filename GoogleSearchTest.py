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
driver.find_element(By.ID, "newPage").click()
print(driver.title)
current_window = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window:
        driver.switch_to.window(window)

print(driver.title)
driver.switch_to.window(current_window)
print(driver.title)

# driver.find_element(By.ID, "clickOnMe").click()
# driver.switch_to.alert.accept()
# # driver.switch_to.alert.dismiss() #albo dismiss albo accept używamy
# driver.find_element(By.ID, "fname").send_keys("Iwonka")
# print("Element text: " + driver.find_element(By.ID, "fname").get_attribute("value"))
# time.sleep(1)
# # driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
# auto_select = Select(driver.find_element(By.TAG_NAME, "select"))
# auto_select.select_by_visible_text("Volvo")
# auto_select.select_by_value("saab")
# auto_select.select_by_index(0)
# driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@value='male']").click()
# time.sleep(1)
# print(driver.find_element(By.XPATH, "//input[@value='male']").text) #brak tesktu więc nie zostanie nic zwrócone
# print(driver.find_element(By.TAG_NAME, "h1").text)
# print(driver.find_element(By.ID, "clickOnMe").text)
# print(driver.find_element(By.TAG_NAME, "p").get_attribute("textContent")) #brak tekstu bo element jest ukryty

# print(driver.find_element(By.ID, "smileImage").size.get("height"))
# print(driver.find_element(By.ID, "smileImage").get_attribute("naturalHeight"))

# click_me_button = driver.find_element(By.ID, "clickOnMe")
# click_me_button.click()

# driver.find_element(By.ID, "fname")
# driver.find_element(By.NAME, "fname")
# driver.find_element(By.LINK_TEXT, "Visit W3Schools.com!")
# driver.find_element(By.PARTIAL_LINK_TEXT, "Visit W3Schools.com") #znajdzie częściowy link,nie trzeba podawać całego linku
# driver.find_element(By.CLASS_NAME, "topSecret")
# # driver.find_element(By.CLASS_NAME, "druga")
# driver.find_element(By.TAG_NAME, "a")
# driver.find_element(By.TAG_NAME, "p")
# driver.find_element(By.TAG_NAME, "label")
# driver.find_element(By.CSS_SELECTOR, "a")
# driver.find_element(By.CSS_SELECTOR, "img#smileImage")
# driver.find_element(By.CSS_SELECTOR, "p.topSecret")
# print(driver.find_element(By.CSS_SELECTOR, "th:first-child").text)
# driver.find_element(By.XPATH, "/html/body/table/tbody/tr/th")
# driver.find_element(By.XPATH, "//th")
# driver.find_element(By.XPATH, "//th[text()='Month']")
# driver.find_element(By.XPATH, "//button[@id='clickOnMe']")
# driver.find_element(By.XPATH, "//input[@id='fname']/following-sibling::table")
# driver.find_element(By.XPATH, "//input[@name='fname']/following-sibling::table")
# element_List = len(driver.find_elements(By.XPATH, "//th"))
# print(element_List)

driver.quit()