import unittest
from selenium.common.exceptions import NoSuchElementException
import sys
import page_factory_for_buyme_test


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.page_factory = page_factory_for_buyme_test.PageFactory()
        cls.page_factory.init_driver()
        cls.driver = cls.page_factory.driver
        cls.page_factory.open_buyme_website()

    def test_regist_to_buyme(self):
        self.page_factory.insert_name()
        self.page_factory.insert_email()
        self.page_factory.insert_password()
        self.page_factory.insert_confirm_password()
        self.page_factory.registration()

        try:
            self.driver.find_element_by_id("ember1530")
            flag = True
        except NoSuchElementException:
            flag = False
        self.assertTrue(flag, "attempt to register to the 'buyme' site id filed")
        #TODO: check this test
        # self.assertEqual(self.driver.title, self.page_factory.DATA['excepted_title'])


def main(out):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out).run(suite)


if __name__ == '__main__':
    with open('byuMe_test_result.txt', 'w') as f:
        main(f)
