from selenium import webdriver
import locators as L
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException,StaleElementReferenceException
from selenium.webdriver.common.by import By
import time

class Cleartrip:

    def __init__(self):
        self.driver = webdriver.Chrome("C:\Work\study\chromedriver_win32\chromedriver.exe")
        self.driver.get("http://www.cleartrip.com")

    @property
    def Flight(self):
        return self.driver.find_element_by_xpath(L.Flights)

    def Enter_Flight_Details(self):
        self.driver.find_element_by_xpath(L.RoundTrip).click()
        self.driver.find_element_by_id(L.Fromtag).click()
        self.driver.find_element_by_id(L.Fromtag).send_keys("Bangalore")
        self.driver.find_element_by_id(L.ToTag).click()
        self.driver.find_element_by_id(L.ToTag).send_keys("Pune")
        self.driver.find_element_by_id(L.DepartDate).click()
        self.driver.find_element_by_id(L.DepartDate).send_keys("1/12/2017")
        self.driver.find_element_by_id(L.ReturnDate).click()
        self.driver.find_element_by_id(L.ReturnDate).send_keys("10/12/2017")
        Select(self.driver.find_element_by_id(L.Numofpassenger)).select_by_visible_text('1')
        self.driver.find_element_by_id(L.SearchBtn).click()

    def Select_Flight(self):
        try:
            WebDriverWait(self.driver,10,poll_frequency=1, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException]).until(EC.presence_of_element_located((By.XPATH,L.book_origin)))
        except:
            pass
        self.driver.execute_script(L.book)

    def Itinerary(self):
        # self.driver.get("https://www.cleartrip.com/flights/itinerary/687edd13ba-f1b3-469c-b37c-62d92a8268a3/review")
        self.driver.find_element_by_id(L.conditions).click()
        self.driver.find_element_by_id(L.itinerary).click()

    def User_Email(self):
        time.sleep(3)
        self.driver.find_element_by_id(L.Username).click()
        self.driver.find_element_by_id(L.Username).send_keys("abcd@abcd.com")
        self.driver.find_element_by_id(L.Log_continue).click()

    def Traveler_Details(self):
        time.sleep(2)
        Select(self.driver.find_element_by_id(L.adult_title)).select_by_visible_text('Mr')
        self.driver.find_element_by_id(L.adult_fname).click()
        self.driver.find_element_by_id(L.adult_fname).send_keys("Vimal")
        self.driver.find_element_by_id(L.adult_lname).click()
        self.driver.find_element_by_id(L.adult_lname).send_keys("Patidar")
        self.driver.find_element_by_id(L.mobile).click()
        self.driver.find_element_by_id(L.mobile).send_keys("918663423411")
        self.driver.find_element_by_id(L.traveller_btn).click()

c = Cleartrip()
# c.Enter_Flight_Details()
# c.Select_Flight()
c.Itinerary()
c.User_Email()
c.Traveler_Details()

