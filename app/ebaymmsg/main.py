

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

from app.ebaymmsg.add_name_to_db import addtodatabase


spam_message = "hello"



def main():

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path="/home/bot/EbayBot/venv/lib/python3.5/geckodriver")
    driver.set_window_size(1280, 850)

    # go to find an ending auction
    try:
        driver.get('http://www.lastminute-auction.com/')
        window_before = driver.window_handles[0]
        print(window_before)
        get_first_element_in_table = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[6]/table/tbody/tr[10]/td[1]/a")
        get_first_element_in_table.click()
        driver.save_screenshot('0.png')
    except Exception as e:
        print("*********error getting table ebay link*********")
        print(str(e))
        driver.save_screenshot('0f.png')

    time.sleep(10)

    try:
        # switch to open window
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        print(window_after)

        # fake attempt to contact seller
        driver.save_screenshot("1.png")
        # click the contact seller box
        click_contact_seller = driver.find_element_by_css_selector(
            "span.no-wrap:nth-child(4) > a:nth-child(1)")
        click_contact_seller.click()
        time.sleep(4)
        driver.save_screenshot("2.png")


        # LOGIN
        driver.save_screenshot('0-1.png')
        username_form = driver.find_element_by_name("userid")
        username_form.clear()
        username_form.send_keys(username)
        password_form = driver.find_element_by_name("pass")
        password_form.clear()
        password_form.send_keys(password)
        submit = driver.find_element_by_id("sgnBt")
        driver.save_screenshot('login-success.png')
        submit.click()

        time.sleep(5)
        print("logged in as: ", username)

    except Exception as e:
        driver.save_screenshot('login-failure.png')
        print(str(e))


    try:
        driver.save_screenshot('redirectafterlogin.png')
        # Topic and next button
        other_circle = driver.find_element_by_xpath(
            '//*[@id="Other"]')
        other_circle.click()
    except Exception as e:
        print(str(e))

    time.sleep(1)

    try:
        hidden_contact_seller_button = driver.find_element_by_xpath(
            '//*[@id="contactSeller"]')
        hidden_contact_seller_button.click()

        time.sleep(3)
        driver.save_screenshot("3f.png")
    except Exception as e:
        print("*********error finding contact seller button*********")
        print(str(e))

    try:
        # get the username
        sellerheader = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div/div/h1/span').text
        print(sellerheader)

        listed_name = sellerheader[8:]
        string_of_the_name = str(listed_name)
        print(string_of_the_name)
    except Exception as e:
        string_of_the_name =  None
        print("*********error finding sellers name*********")
        print(str(e))

    try:
        # click the send message box
        message_box = driver.find_element_by_xpath(
            '//*[@id="msg_cnt_cnt"]')
        message_box.click()


        # MESSAGE
        #
        message_box.send_keys(spam_message)
        ##

        # click the send message
        message_box = driver.find_element_by_xpath(
            '//*[@id="sndBtn"]')
        driver.save_screenshot("4.png")
        #message_box.click()

    except Exception as e:
        print("*********error sending message*********")
        print(str(e))
    try:
        if string_of_the_name is not None:
            addtodatabase(username=string_of_the_name)
            driver.save_screenshot("5.png")
        else:
            pass
    except Exception as e:
        print("*********error adding to db*********")
        print(str(e))
    driver.quit()


