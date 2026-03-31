#Task 4 : Selenium with Pytest or Pytest Playwright automation

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()


def test_input_box(driver):

    input_box = driver.find_element(By.ID, "name")
    input_box.clear()
    input_box.send_keys("Akshay")
    assert input_box.get_attribute("value") == "Akshay"


def test_radio_button(driver):

    radio = driver.find_element(By.XPATH, "//input[@value='radio2']")
    radio.click()
    assert radio.is_selected()


def test_dropdown(driver):

    dropdown = driver.find_element(By.ID, "dropdown-class-example")
    option = driver.find_element(By.XPATH, "//option[@value='option2']")
    option.click()
    assert option.is_selected()