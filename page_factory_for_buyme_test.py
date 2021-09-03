import create_xml_config
from lxml import etree as et
from selenium import webdriver

class PageFactory():
    DATA = {}

    @staticmethod
    def data_from_xml_config():
        create_xml_config.create_xml_file()
        contents_xml_file = et.parse('config_xml_for_buyme.xml')
        for items in contents_xml_file.iter():
            PageFactory.DATA[items.tag] = items.text

    def __init__(self):
        PageFactory.data_from_xml_config()
        self.name = PageFactory.DATA['first_name']
        self.expected_title = PageFactory.DATA['excepted_title']
        self.email = PageFactory.DATA['mail']
        self.password = PageFactory.DATA['password']
        self.confirm_password = PageFactory.DATA['password_confirm']
        self.driver = self.init_driver()

    def init_driver(self):
        driver = None
        if PageFactory.DATA['browser_type'] == 'Chrome':
            driver = webdriver.Chrome()
        elif PageFactory.DATA['browser_type'] == 'Edge':
            driver = webdriver.Edge()
        buyme_url = 'https://buyme.co.il/'
        driver.get(buyme_url)
        return driver


    def open_buyme_website(self):
        self.driver.find_element_by_class_name('seperator-link').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span').click()
        self.driver.implicitly_wait(1)

    def insert_name(self):
        self.driver.find_element_by_id("ember1482").send_keys(self.name)
        self.driver.implicitly_wait(1)

    def insert_email(self):
        self.driver.find_element_by_id("ember1485").send_keys(self.email)
        self.driver.implicitly_wait(1)

    def insert_password(self):
        self.driver.find_element_by_id("valPass").send_keys(self.password)
        self.driver.implicitly_wait(1)

    def insert_confirm_password(self):
        self.driver.find_element_by_id("ember1491").send_keys(self.confirm_password)
        self.driver.implicitly_wait(1)

    def registration(self):
        self.driver.find_element_by_id('ember1493').click()
        self.driver.implicitly_wait(1)



