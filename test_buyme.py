import unittest
from selenium.common.exceptions import NoSuchElementException
import sys
from create_xml_config import CreateConfig
import random
from lxml import etree as et
import page_factory_for_buyme_test
from selenium import webdriver


class ByuMeTest(unittest.TestCase):
    driver = None
    page_factory = None
    DATA = {}

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = ByuMeTest.init_driver()
        cls.page_factory = page_factory_for_buyme_test.PageFactory(cls.driver)

    @staticmethod
    def init_driver():
        driver = None
        if ByuMeTest.DATA['browser_type'] == 'Chrome':
            driver = webdriver.Chrome()
        elif ByuMeTest.DATA['browser_type'] == 'Edge':
            driver = webdriver.Edge()
        buyme_url = 'https://buyme.co.il/'
        driver.maximize_window()
        driver.get(buyme_url)
        return driver

    def test_regist_to_buyme(self):
        self.page_factory.insert_name(ByuMeTest.DATA["first_name"])
        self.page_factory.insert_email(ByuMeTest.DATA["mail"])
        self.page_factory.insert_password(ByuMeTest.DATA["password"])
        self.page_factory.insert_confirm_password(ByuMeTest.DATA["password_confirm"])
        self.page_factory.registration()

        # check if the botton 'החשבון שלי' is exists
        try:
            self.driver.find_element_by_id("ember1530")
            flag = True
        except NoSuchElementException:
            flag = False
        self.assertTrue(flag, "attempt to register to the 'buyMe' site id filed")
        self.assertEqual(self.driver.title, ByuMeTest.DATA['excepted_title'])


#####------------------- main function --------------------####

browser_options = ["Chrome", "Edge"]
first_name_options = ["Itzhak", "Jek", "Sami", "Josh"]

INPUT = {"browser_type": random.choice(browser_options),
         "excepted_title": "BUYME אתר המתנות והחוויות הגדול בישראל |\xa0Gift Card",
         "first_name": random.choice(first_name_options),
         'mail': f"{random.randint(1111111111, 99999999999)}@gmail.com",
         "password": "Abcd1234",
         "password_confirm": "Abcd1234"}


def create_xml_file():
    config = CreateConfig("buy_me_website")
    for key, value in INPUT.items():
        config.add_child(key, INPUT[key])
    config.write_to_file("config_xml_for_buyme.xml")


def data_from_xml_config():
    contents_xml_file = et.parse('config_xml_for_buyme.xml')
    for items in contents_xml_file.iter():
        ByuMeTest.DATA[items.tag] = items.text


def main(out):
    create_xml_file()
    data_from_xml_config()

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out).run(suite)


if __name__ == '__main__':
    with open('byuMe_test_result.txt', 'w') as f:
        main(f)
