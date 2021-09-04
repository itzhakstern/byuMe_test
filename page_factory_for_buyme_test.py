

class PageFactory:
    def __init__(self, driver):
        self.__driver = driver
        self.open_buyme_website()

    def open_buyme_website(self):
        self.__driver.find_element_by_class_name('seperator-link').click()
        self.__driver.implicitly_wait(1)
        self.__driver.find_element_by_xpath('//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span').click()
        self.__driver.implicitly_wait(1)

    def insert_name(self, name):
        self.__driver.find_element_by_id("ember1482").send_keys(name)
        self.__driver.implicitly_wait(1)

    def insert_email(self, email):
        self.__driver.find_element_by_id("ember1485").send_keys(email)
        self.__driver.implicitly_wait(1)

    def insert_password(self, password):
        self.__driver.find_element_by_id("valPass").send_keys(password)
        self.__driver.implicitly_wait(1)

    def insert_confirm_password(self, confirm_password):
        self.__driver.find_element_by_id("ember1491").send_keys(confirm_password)
        self.__driver.implicitly_wait(1)

    def registration(self):
        self.__driver.find_element_by_id('ember1493').click()
        self.__driver.implicitly_wait(1)
