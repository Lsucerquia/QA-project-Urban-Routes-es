import data
from urban_routes_page import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs",{"performance":"ALL"})
        cls.driver = webdriver.Chrome(service=Service(),options=options)
    
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        self.driver.get(data.urban_routes_url) 
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        time.sleep(2)

    def test_set_phone_number(self):
        self.driver.get(data.urban_routes_url) 
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone(data.phone_number)
        time.sleep(2)

    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url) 
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone(data.phone_number)
        routes_page.add_credit_card(data.card_number,data.card_code)
        time.sleep(5)

    def test_write_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone(data.phone_number)
        routes_page.add_credit_card(data.card_number,data.card_code)
        routes_page.set_driver_message_field(data.message_for_driver)
        assert routes_page.get_driver_message_field().get_property('value') == data.message_for_driver
        time.sleep(4)

    def test_request_blanket_and_tissues(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone(data.phone_number)
        routes_page.add_credit_card(data.card_number,data.card_code)
        routes_page.set_driver_message_field(data.message_for_driver)
        routes_page.click_blanket_and_tissues_toggle()
        time.sleep(4)


    def test_order_two_ice_creams(self):
         self.driver.get(data.urban_routes_url)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.set_route(data.address_from, data.address_to)
         routes_page.select_comfort_tariff()
         routes_page.set_phone(data.phone_number)
         routes_page.add_credit_card(data.card_number,data.card_code)
         routes_page.set_driver_message_field(data.message_for_driver)
         routes_page.click_blanket_and_tissues_toggle()
         routes_page.click_ice_cream_plus()
         routes_page.click_ice_cream_plus()
         time.sleep(4)

    def test_order_taxi_modal_appears(self):
         self.driver.get(data.urban_routes_url)
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.set_route(data.address_from, data.address_to)
         routes_page.select_comfort_tariff()
         routes_page.set_phone(data.phone_number)
         routes_page.add_credit_card(data.card_number,data.card_code)
         routes_page.set_driver_message_field(data.message_for_driver)
         routes_page.click_blanket_and_tissues_toggle()
         routes_page.click_ice_cream_plus()
         routes_page.click_ice_cream_plus()
         routes_page.open_taxi_modal()
         assert routes_page.get_taxi_modal().is_displayed()
         time.sleep(4)


    def test_modal_driver_information(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.select_comfort_tariff()
        routes_page.set_phone(data.phone_number)
        routes_page.add_credit_card(data.card_number,data.card_code)
        routes_page.set_driver_message_field(data.message_for_driver)
        routes_page.click_blanket_and_tissues_toggle()
        routes_page.click_ice_cream_plus()
        routes_page.click_ice_cream_plus()
        routes_page.open_taxi_modal()
        assert routes_page.get_driver_info_modal().is_displayed()
        print(hasattr(routes_page, "get_driver_info_modal"))
        time.sleep(4)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
