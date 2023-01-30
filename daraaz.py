from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.daraz.com.np/laptops/?min_price=300000"

# Start a new browser instance
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-card")))

# Extract the laptops
laptops = driver.find_elements_by_css_selector(".product-card")
for laptop in laptops:
    name = laptop.find_element_by_css_selector(".title").text
    price = laptop.find_element_by_css_selector(".price").text
    if int(price.replace(',',''))>100000:
        print(name + ': ' + price)

# Close the browser instance
driver.quit()
