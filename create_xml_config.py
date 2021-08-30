from lxml import etree as et
import random

browser_options = ["Chrome", "Edge"]
first_name_options = ["Itzhak", "Jek", "Sami", "Josh"]

INPUT = {"browser_type": random.choice(browser_options),
         "excepted_title": "BUYME אתר המתנות והחוויות הגדול בישראל | Gift Card",
         "first_name": random.choice(first_name_options),
         'mail': f"{random.randint(1111111111,99999999999)}@gmail.com",
         "password": "Abcd1234",
         "password_confirm": "Abcd1234"}


class CreateConfig:

    def __init__(self, root_name):
        self.__root = et.Element(root_name)
        self.__tree = et.ElementTree(self.__root)

    def add_child(self, tag_name, text):
        et.SubElement(self.__root, tag_name).text = text

    def write_to_file(self, file_name):
        self.__tree.write(file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')


def create_xml_file():
    config = CreateConfig("buy_me_website")
    for key, value in INPUT.items():
        config.add_child(key, INPUT[key])
    config.write_to_file("config_xml_for_buyme.xml")

