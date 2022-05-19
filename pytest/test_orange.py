import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome("G:\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        status = self.driver.find_element(By.XPATH, "//*[@id='divLogo']/img").is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome("G:\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        title = self.driver.title

        if title == "OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach("self.driver.get_screenshot_as_png()", name="TestLoginScreen", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_list_employees(self):
        pytest.skip("skipping list of employees bcoz at this time it is not necessary")


