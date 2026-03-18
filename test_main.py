from selenium import webdriver
from selenium.webdriver.common.by import By

def valid_login(user,passwords):
    driver = webdriver.Chrome()
    page_url = "https://www.saucedemo.com/"
    driver.get(page_url)
    username=driver.find_element(By.ID,"user-name")
    username.send_keys(user)
    password=driver.find_element(By.ID,"password")
    password.send_keys(passwords)
    login=driver.find_element(By.ID,"login-button")
    login.click()
    return driver

def test_valid_title():
    driver=valid_login("standard_user","secret_sauce")
    assert "Swag Labs" in driver.title
    driver.quit()

def test_invalid_title():
    driver=valid_login("standard_user","secret_sauce")
    assert "Swag labs" in driver.title
    driver.quit()

def test_valid_homepage():
    driver=valid_login("standard_user","secret_sauce")
    assert "https://www.saucedemo.com/" in driver.current_url
    driver.quit()
def test_invalid_homepage():
    driver=valid_login("standard_user","secret_sauce")
    assert "https://www.saucedemos.com/" in driver.current_url
    driver.quit()
def test_valid_dashboard():
    driver=valid_login("standard_user","secret_sauce")
    assert "https://www.saucedemo.com/" in driver.current_url
    driver.quit()
def test_invalid_dashboard():
    driver=valid_login("standard_user","secret")
    assert "https://www.saucedemo.com/" in driver.current_url
    driver.quit()
#pytest --html=report.html
