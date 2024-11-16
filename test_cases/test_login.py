from pytest_html.extras import image
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


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

        act_verify_login_page = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[1]/div[2]').text
        exp_verify_login_page = "Masuk Terbaru"
        if act_verify_login_page == exp_verify_login_page:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False