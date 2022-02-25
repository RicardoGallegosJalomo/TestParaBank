import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones
from Funciones.Funciones import Funciones_Globales

tie = 2

def setup_function(function):
    print("\nInicia Test")
    global driver, func
    driver = webdriver.Chrome(executable_path="C:/driverchrome/chromedriver.exe")

    func = Funciones_Globales(driver)
    func.navegar("https://parabank.parasoft.com/parabank/index.htm", tie)
    driver.maximize_window()

def teardown_function(function):
    print("Finaliza Test")
    driver.close()

def test_about():

    func.click_xpath_val("(//a[@href='about.htm'][contains(.,'About Us')])[1]",tie)
    func.text_xpath_val("//input[contains(@type,'text')]","john",tie)
    func.text_xpath_val("//input[contains(@type,'password')]","demo",tie)
    func.click_xpath_val("//input[contains(@type,'submit')]",tie)

def test_services():

    func.click_xpath_val("(//a[contains(.,'Services')])[1]",tie)
    el1 = func.Selector_xpath("//span[@class='heading'][contains(.,'Available Bookstore SOAP services:')]")
    el1 = el1.text
    if el1 == "Available Bookstore SOAP services:":
        print("La prueba de Service es correcta")
    else:
        print("Validacion de Service es incorrecta")

    el2 = func.Selector_xpath("//span[@class='heading'][contains(.,'Bookstore services:')]")
    el2 = el2.text
    if el2 == "Bookstore services:":
        print("La prueba de Bookstore service es correcta")
    else:
        print("La prueba de Bookstore service es incorrecta")

    func.click_xpath_val("(//a[@href='http://www.parasoft.com/jsp/products.jsp'][contains(.,'Products')])[1]",tie)
    driver.back()
    func.click_xpath_val("(//a[@href='http://www.parasoft.com/jsp/pr/contacts.jsp'][contains(.,'Locations')])[1]",tie)
    driver.back()
    func.click_xpath_val("//a[@href='admin.htm'][contains(.,'Admin Page')]",tie)
    elemento3 = func.Selector_xpath("//h2[contains(.,'Customer Login')]")
    elemento3 = elemento3.text
    if elemento3 == "Customer Login":
        print("Entrada a Login Correcta")
    else:
        print("No entro a Login")
    func.text_xpath_val("//input[contains(@name,'username')]","Ricardo",tie)
    func.text_xpath_val("//input[contains(@type,'password')]","1234567",tie)
    func.click_xpath_val("//input[contains(@type,'submit')]",tie)
    elemento4 = func.Selector_xpath("//p[@class='error']"
                                    "[contains(.,'The username and password could not be verified.')]")
    elemento4 = elemento4.text
    print(elemento4)
    if elemento4 == "The username and password could not be verified.":
        print("Atrapo Error de login Correcta funciona el login")
    else:
        print("Fallo la prueba de Login")
    func.text_xpath_val("//input[contains(@name,'username')]", "john", tie)
    func.text_xpath_val("//input[contains(@type,'password')]", "demo", tie)
    func.click_xpath_val("//input[contains(@type,'submit')]", tie)

def test_correo():

    func.click_xpath_val("//a[contains(.,'contact')]",tie)
    func.text_xpath_val("//input[contains(@id,'name')]","Ricardo Gallegos",tie)
    func.text_xpath_val("//input[contains(@id,'email')]","ricardo@gmail.com",tie)
    func.text_xpath_val("//input[contains(@id,'phone')]","556677889911",tie)
    func.text_xpath_val("//textarea[contains(@id,'message')]","Esta es una prueba de mensaje",tie)
    func.click_xpath_val("//input[contains(@value,'Send to Customer Care')]",tie)
