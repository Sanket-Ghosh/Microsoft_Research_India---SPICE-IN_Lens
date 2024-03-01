from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

service = Service(executable_path="chromedriver.exe")

# Set up the Chrome webdriver with options to disable the PDF viewer
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
        "plugins.always_open_pdf_externally": True
    })
    
driver = webdriver.Chrome(service= service, options=chrome_options)



driver.get("https://arxiv.org/")
time.sleep(5)

click_element = driver.find_element(By.ID, "new-cs").click()
click_element = driver.find_element(By.CLASS_NAME, "list-identifier").click()
click_element = driver.find_element(By.CLASS_NAME, "abs-button.download-pdf").click()
pdf_link = driver.find_element(By.XPATH, '//a[contains(@href, ".pdf")]').get_attribute('href')


# Downloading The PDF file
save_path = 'latest.pdf'


time.sleep(5)


driver.quit()

