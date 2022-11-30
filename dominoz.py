# selenium - Web scraping and automation library. You can install it using pip install selenium.
# Now we need to install a webdriver. A webdriver is a collection of open source API which are used to automate testing of a web application. Click on three dots on upper left side of the page. go to help and go to about chrome. Check the version of chrome and install that versions chrome driver. 
# After installing it copy its .exe file and place it on the dekstop.
#importing modules-->
import time
from selenium import webdriver
from time import sleep
from scully import speak, takecommand

def pizza():
    driver = webdriver.Chrome(r"C:\Users\DJM21\Desktop\chromedriver.exe")   #copy the location of the .exe file and paste it here and add chromedriver.exe at last. If you will run this program till here, a window will appear whcih will be non maximize. 
    driver.maximize_window()   #to maximize window

    speak("Opening dominos website sir!")
    driver.get('https://www.dominos.co.in/')
    sleep(2)    #We need to use sleep because as soon as we run the program it will close the window. this will make sure it will open the sit till 2 second.

    speak("Getting reading to order sir!")
    driver.find_element_by_link_text('ORDER ONLINE NOW').click()
    sleep(2)

    speak("Finding your location sir!")
    driver.find_element_by_class_name('srch-cnt-srch-inpt').click()      #while finding the location,right click on it, click on inspect and you will get an input class tag. Copy the class name and paste it in here.
    sleep(2)

    #To enter location we need to create a variable -->
    speak("Entering your location sir!")
    location =  "Ratna Jyoti Apartments"

    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(location)  #Before giving the location you need to copy its xpath. Go to inspect and copy the xpath 
    sleep(2)

    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div[2]/span[1]').click()
    sleep(2)

    driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[1]').click()
    sleep(2)

    speak("logging into the website sir!")
    phone_number =  "9974313351"
    driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(phone_number)
    sleep(2)

    driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
    sleep(2)

    speak("Sir, What is your OTP?")
    sleep(3)

    otp_log = takecommand()

    driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(otp_log)
    sleep(2)

    # submitting the otp
    driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()
    sleep(2)

    speak("Ordering peppy paneer pizza sir")
    driver.find_element_by_xpath('//*[@id="mn-lft"]/div[2]/div/div[3]/div/div/div[2]/div[3]/div/button/span').click()
    sleep(2)
     
    driver.find_element_by_xpath('//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
    sleep(2)

    driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button').click()
    sleep(30)




pizza()    
