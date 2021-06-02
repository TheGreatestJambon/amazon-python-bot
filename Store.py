from selenium import webdriver  # Connects you to a browser's instance

from selenium.webdriver.common.keys import Keys  # Keys emulate the stroke of keyboard keys
from selenium.webdriver.common.action_chains import ActionChains  # Automation of mouse movement, drag and drop etc
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, \
    StaleElementReferenceException, ElementClickInterceptedException  # Handle Exceptions
from random import randint, randrange  # Important functions to wait and randomise actions
import time
import random
import Globals
import UI
from sys import exit

class Store:
    def __init__(self, username, password):
        """ Initialise the bot with class-wide attributes. """
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    # Open the browser and navigate to the given URL
    def openBrowser(self):
        """ Finds the product with a global link. """
        self.driver.maximize_window()
        try:
            self.driver.get(Globals.URL)
        except:
            print('URL is incorrect, closing...')
            self.closeBrowser()
        time.sleep(1)
        self.buyProduct()

    # Find product under or equal to X amount
    def buyProduct(self):
        """ Proceeds to checkout and purchase for item. """
        driver = self.driver  # Localise the variable for use
        price_indicator = 0  # To indicate which type of price is being compared

        # Determination of whether the 'Buy Now' or 'All-Buying-Choices' element is displayed
        try:
            buy_box = driver.find_element_by_id('buybox-see-all-buying-choices')
        except NoSuchElementException:
            print('No Buy_Box Found')
        else:
            buy_box.click()
            price_indicator = 1

        if not price_indicator == 1:
            price_indicator = 2

        # Check if the product is available, as well as its price
        isAvailable = self.isProductAvailable(price_indicator)

        # If product is unavailable, wait until it is
        if isAvailable == 'Currently unavailable.':
            self.refreshPage()  # Repeat the process

        # Buy Now
        if isAvailable <= Globals.PRICE_LIMIT:

            if price_indicator == 1:
                add_basket = driver.find_element_by_name('submit.addToCart')
                add_basket.click()
                time.sleep(randint(int(Globals.WAIT_TIME / 2), Globals.WAIT_TIME))
                go_checkout = driver.find_element_by_id('hlb-ptc-btn-native')  # Proceed to checkout button
                go_checkout.click()
                self.signIn()  # Call the sign in method with the relevant instance passed in
            elif price_indicator == 2:
                buy_now = driver.find_element_by_id('buy-now-button')  # Find the buy now button by id
                element_y = (buy_now.location['y'])  # Location of Buy_Now element
                window_h = driver.execute_script('return window.innerHeight')
                desired_y = element_y - (window_h / 2)

                # Attempt to click buy now button
                for iteration in range(2):
                    try:
                        buy_now.click()
                    except ElementClickInterceptedException:
                        print('Element is obscured, scrolling...')
                        for i in range(int(desired_y)):  # To avoid the cookie banner
                            driver.execute_script("window.scrollBy(0, 1)")
                    else:
                        break

                self.signIn()  # Call the sign in method with the relevant instance passed in

                # Place Order
                place_order = driver.find_element_by_name('placeYourOrder1').text
                time.sleep(randint(int(Globals.WAIT_TIME / 2), Globals.WAIT_TIME))
                place_order.click()  # Click the place_order button
                time.sleep(randint(int(Globals.WAIT_TIME / 2), Globals.WAIT_TIME))

        else:  # If Product is over max price
            time.sleep(randint(int(Globals.WAIT_TIME / 2), Globals.WAIT_TIME))
            self.refreshPage()  # Repeat the process

    # Refresh the page
    def refreshPage(self):
        driver = self.driver
        driver.get(driver.current_url)
        time.sleep(randint(int(7 / 2), 7))
        driver.refresh()
        self.buyProduct()

    # Sign into site with the product
    def signIn(self):
        """ Sign into site with the product """
        driver = self.driver

        # Enter Username
        time.sleep(randint(int(Globals.WAIT_TIME / 2), Globals.WAIT_TIME))
        username_elem = driver.find_element_by_xpath("//input[@name='email']")  # Find username element
        username_elem.clear()  # Clear the username field
        user_val = self.username

        # Simulation of typing letter by letter
        for i in range(0, len(user_val)):
            user_string = ""
            user_string += user_val[i]
            username_elem.send_keys(user_string)  # Send the username to the browser
            time.sleep(0.1)
        username_elem.send_keys(Keys.RETURN)
        time.sleep(1)
        try:
            error_display = driver.find_element_by_id('auth-error-message-box').is_displayed()
        except:
            pass
        else:
            print('User/Email is incorrect, closing...')
            self.closeBrowser()

        # Enter Password
        time.sleep(randint(int(Globals.WAIT_TIME / 2), Globals.WAIT_TIME))
        password_elem = driver.find_element_by_xpath("//input[@name='password']")  # Find password element
        password_elem.clear()  # Clear the password field
        pass_val = self.password

        for i in range(0, len(pass_val)):
            pass_string = ""
            pass_string += pass_val[i]
            password_elem.send_keys(pass_string)
            time.sleep(0.1)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(1)
        try:
            error_display = driver.find_element_by_id('auth-error-message-box').is_displayed()
        except:
            pass
        else:
            print('Password is incorrect, closing...')
            self.closeBrowser()

    def isProductAvailable(self, indicator):
        """ Checks if product is available. """
        driver = self.driver  # Localise the variable for use
        if indicator == 1:
            time.sleep(randint(int(Globals.WAIT_TIME / 2), Globals.WAIT_TIME))
            price = driver.find_element_by_xpath("//span[@class = 'a-price-whole']").text  # Search for the span element within the class name.

            for comma in price:  # Remove the comma from the price
                new_price = price.replace(",", "")
            print(f'***** PRICE: {new_price}')
            return float(new_price)
        elif indicator == 2:
            available = driver.find_element_by_class_name('a-color-price').text  # Will return "Currently Unavailable" or Product Price
            if available == 'Currently unavailable.':
                print(f'***** AVAILABLE: {available}')
                return available  # Return if unavailable.
            else:
                print(f'***** PRICE: {available}')
                return float(available[1:])  # Needs to be cast in order to use for numeric price comparison, currency symbol cannot be compared so 1st character is ignored.

    def closeBrowser(self):  # Close the browser
        """ Closes browser """
        Globals.PASS = ""
        Globals.PRICE_LIMIT = ""
        Globals.USER = ""
        Globals.URL = ""
        self.driver.quit()
        exit()


if __name__ == '__main__':
    storeBot = Store(username=Globals.USER, password=Globals.PASS)
    storeBot.openBrowser()
    storeBot.closeBrowser()



