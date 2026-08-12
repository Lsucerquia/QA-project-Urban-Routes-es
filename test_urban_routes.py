import data
from urban_routes_page import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs",{"performance":"ALL"})
        cls.driver = webdriver.Chrome(service=Service(),options=options)
    
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()
        assert  routes_page.get_selected_tariff() == 'Comfort'
        

    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone(data.PHONE_NUMBER)
        assert routes_page.get_phone_number_display() == data.PHONE_NUMBER

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_credit_card(data.CARD_NUMBER,data.CARD_CODE)
        assert routes_page.get_current_payment_method_text() == 'Tarjeta'
        

    def test_write_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_driver_message_field(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_driver_message_field().get_property('value') == data.MESSAGE_FOR_DRIVER
        

    def test_request_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_tissues_toggle()
        assert routes_page.get_blanket_and_tissues_checked()
        

    def test_order_two_ice_creams(self):
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.click_ice_cream_plus()
         routes_page.click_ice_cream_plus()
         assert routes_page.get_ice_cream_counter_value() == 2

    def test_order_taxi_modal_appears(self):
         routes_page = UrbanRoutesPage(self.driver)
         routes_page.open_taxi_modal()
         assert routes_page.get_taxi_modal().is_displayed()
        

    def test_modal_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_driver_info_modal().is_displayed()
        

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
