from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
username=driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")
password=driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
login=driver.find_element(By.ID,"login-button")
login.click()
print("THE TITLE OF THE WEBPAGE IS: ",driver.title)
print("THE CURRENT URL OF THE WEBPAGE IS: ",driver.current_url)
text=driver.find_element(By.TAG_NAME,"body").text
#text=driver.page_source

with open("webpage_task_11.txt","w",encoding="utf-8")as file:
    file.write(text)

# with open("webpage_task_11.txt","r",encoding="utf-8")as file:
#     print(file.read())

