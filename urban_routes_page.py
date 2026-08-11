from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    #localizadoreS
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR,'.button.round')
    comfort_icon = (By.XPATH,"//div[@class='tcard-title' and text()='Comfort']")
    phone_field = (By.CSS_SELECTOR,".np-text")
    phone_input = (By.ID,"phone")
    phone_next_button = (By.XPATH,"//button[text()='Siguiente']")
    phone_code_field = (By.ID,"code")
    confirm_code_button = (By.XPATH,"//button[@type='submit' and normalize-space(text())='Confirmar']")
    payment_method_field = (By.CSS_SELECTOR,"div.pp-button.filled")
    add_card_field = (By.XPATH,"//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.ID,"number")
    card_cvv_field = (By.CSS_SELECTOR, ".card-code-input #code")
    add_card_button = (By.XPATH,"//button[@type='submit' and text()='Agregar']")
    close_payment_method_button = (By.XPATH,"//div[@class='section active'][.//div[@class='head' and text()='Método de pago']]//button[@class='close-button section-close']")
    driver_message_field = (By.ID,"comment")
    blanket_and_tissues_toggle = (By.XPATH,"//div[@class='r-sw-container'][.//div[text()='Manta y pañuelos']]//span[@class='slider round']")
    ice_cream_plus =(By.XPATH,"//div[contains(@class,'r-counter')][.//div[contains(@class,'r-counter-label') and text()='Helado']]//div[contains(@class,'counter-plus')]")
    order_taxi_button =(By.CSS_SELECTOR,".smart-button")
    taxi_modal = (By.CSS_SELECTOR,".order-body")
    driver_info_modal =(By.CSS_SELECTOR,".order-number")

    def __init__(self, driver):
        self.driver = driver
    #metodo para Configurar la dirección 
    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)
    

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

     
    def set_route(self,from_address,to_address):
            self.set_from(from_address)
            self.set_to(to_address)

    #metodos Seleccionar la tarifa Comfort.
    def get_request_taxi_button(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.request_taxi_button)    
         )

    def click_request_taxi_button(self):
         self.get_request_taxi_button().click()

    def get_comfort_icon(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.comfort_icon)
         )

    def click_comfort_icon(self):
         self.get_comfort_icon().click()

     
    def select_comfort_tariff(self):
         self.click_request_taxi_button()
         self.click_comfort_icon()

     #metodos para Rellenar el número de teléfono.
    def get_phone_field(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.phone_field)
         )

    def click_phone_field(self):
         self.get_phone_field().click()
    
    def get_phone_input(self):
         return WebDriverWait(self.driver,5).until(
              EC.visibility_of_element_located(self.phone_input)
         )

    def set_phone_input(self,number):
         self.get_phone_input().send_keys(number)


    def get_phone_next_button(self):
      return WebDriverWait(self.driver,5).until(
             EC.element_to_be_clickable(self.phone_next_button)
         )

    def click_phone_next_button(self):
         self.get_phone_next_button().click()

    def get_phone_code_field(self):
         return WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(self.phone_code_field)
         ) 
    
    def set_phone_code_field(self,code):
         self.get_phone_code_field().send_keys(code)

    def get_confirm_code_button(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.confirm_code_button)
         )
    def clik_confirm_code_button(self):
         self.get_confirm_code_button().click()

    def set_phone(self,phone_number):
         self.click_phone_field()
         self.set_phone_input(phone_number)
         self.click_phone_next_button()
         code = retrieve_phone_code(self.driver)
         self.set_phone_code_field(code)
         self.clik_confirm_code_button()

     # metodos para ingresar numero de tarjeta
    def get_payment_method_field(self):
        return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.payment_method_field)
         )

    def click_payment_method_field(self):
         self.get_payment_method_field().click()

    def get_add_card_field(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.add_card_field)
         )

    def click_add_card_field(self):
         self.get_add_card_field().click()

    def get_card_number_field(self):
         return WebDriverWait(self.driver,5).until(
              EC.visibility_of_element_located(self.card_number_field)
         )
    
    def set_card_number_field(self, card_number):
         self.get_card_number_field().send_keys(card_number)

    def get_card_cvv_field(self):
         return WebDriverWait(self.driver,5).until(
              EC.visibility_of_element_located(self.card_cvv_field)
         )
    def set_card_cvv_field(self, card_code):
         self.get_card_cvv_field().send_keys(card_code)
         self.get_card_cvv_field().send_keys(Keys.TAB)
  

    def get_add_card_button(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.add_card_button)
         )
    
    def click_add_card_button(self):
         self.get_add_card_button().click()
         

    def get_close_payment_method_button(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.close_payment_method_button)
         )
    def click_close_payment_method_button(self):
         self.get_close_payment_method_button().click()

    def add_credit_card(self,card_number,card_code):
         self.click_payment_method_field()
         self.click_add_card_field()
         self.set_card_number_field(card_number)
         self.set_card_cvv_field(card_code)
         self.click_add_card_button()
         self.click_close_payment_method_button()

     #metodos para escribir un mensaje al conductor
    def get_driver_message_field(self):
         return WebDriverWait(self.driver,5).until(
              EC.visibility_of_element_located(self.driver_message_field)
         )
    def set_driver_message_field(self,message_for_driver):
         self.get_driver_message_field().send_keys(message_for_driver)

     #metodos para selecionar manta y pañuelos
    def get_blanket_and_tissues_toggle(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.blanket_and_tissues_toggle)
         )
    def click_blanket_and_tissues_toggle(self):
         self.get_blanket_and_tissues_toggle().click()

     #metodos para pedir 2 helados
    def get_ice_cream_plus(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.ice_cream_plus)
         )
    def click_ice_cream_plus(self):
         self.get_ice_cream_plus().click()
         self.get_ice_cream_plus().click()
    
     #metodos para que Aparezca el modal para buscar un taxi.
    def get_order_taxi_button(self):
         return WebDriverWait(self.driver,5).until(
              EC.element_to_be_clickable(self.order_taxi_button)
         )
    def click_order_taxi_button(self):
         self.get_order_taxi_button().click()

    def get_taxi_modal(self):
         return WebDriverWait(self.driver,5).until(
              EC.visibility_of_element_located(self.taxi_modal)
         )

    def open_taxi_modal(self):
     self.click_order_taxi_button()
     self.get_taxi_modal()


     #metodo para ver informacion del conductor en el modal
    def get_driver_info_modal(self):
          return WebDriverWait(self.driver,60).until(
               EC.visibility_of_element_located(self.driver_info_modal)
          )
         

     


         

         

     


         

         
 
            

    
   
    
 