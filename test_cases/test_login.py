from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.test_login_page import Test_Login_Page


class Test_Login_Facebook:
    # Data and Locator
    page_login_url = "https://www.facebook.com/"
    email = "nyupang.me@gmail.com"
    password = "Karlina071802"
    invalid_email = "me@gmail.com"

    # verify page login facebook
    def test_verify_page_login_facebook(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.page_login_url)

        act_verify_login_page = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[1]/h2').text
        exp_verify_login_page = "Facebook helps you connect and share with the people in your life."
        if act_verify_login_page == exp_verify_login_page:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    #test login facebook with valid data
    def test_valid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.page_login_url)

        self.user_tlp = Test_Login_Page(self.driver)
        self.user_tlp.enter_email_xpath(self.email)
        self.user_tlp.enter_password_xpath(self.password)
        self.user_tlp.click_btn_login_xpath()
        act_login_text = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_YX"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[1]/span[2]/span')
        exp_login_text = "Photo/video"
        if act_login_text == exp_login_text:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False