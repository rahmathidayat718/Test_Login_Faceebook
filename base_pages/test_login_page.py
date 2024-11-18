from selenium.webdriver.common.by import By


class Test_Login_Page:

    # Locator
    email_xpath = '//*[@id="email"]'
    password_xpath = '//*[@id="pass"]'
    btn_login_xpath = '//form/div[2]/button'

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action (Instruction)
    def enter_email_xpath(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)
    def enter_password_xpath(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
    def click_btn_login_xpath(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()