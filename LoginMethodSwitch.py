import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class SwitchError(Exception):
    pass

def get_status(url):
    res=urllib.request.urlopen(url)
    page_status=res.getcode()
    return page_status

def LoginMethodSwitch():
    driver=webdriver.Edge()
    url = "https://passport.vip.com/login"
    driver.get(url)
    time.sleep(3)

    try:
        '''切换至账户登录'''
        #driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_xpath("//div[@class='c-tab-nav']/div[2]").click()
        time.sleep(2)

        '''寻找账户登录特征值'''
        target=driver.find_element_by_class_name("i-forget-link")
        if(target):
            print("Passed! - Login Method Switch : VIP Account")
            driver.get_screenshot_as_file("D:\\VIP\\Passed_Login_Method_Switch_1.png")
            time.sleep(2)

            '''切换回扫码登录'''
            print("Switching back to Login by Scanning QR Code...")
            driver.find_element_by_xpath("//div[@class='c-tab-nav']/div[1]").click()
            time.sleep(2)

            target2=driver.find_element_by_class_name("u-text-highlight")
            if(target2):
                print("Passed - Login Method Switch : Scanning QR Code\r")
                driver.get_screenshot_as_file("D:\\VIP\\Passed_Login_Method_Switch_2.png")

                '''鼠标悬停二维码操作'''
                element=driver.find_element_by_class_name("J-qr-img")
                ActionChains(driver).move_to_element(element).perform()
                time.sleep(2)
                driver.get_screenshot_as_file("D:\\VIP\\Hover_Display_QR_Code.png")
                driver.quit()

            else:
                driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Method_Switch_2.png")
                driver.quit()
                raise SwitchError("Failed! - Login Method Switch : QR Code")
        else:
            driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Method_Switch_1.png")
            driver.quit()
            raise SwitchError("Failed! - Login Method Switch : VIP Account")

    except SwitchError as e:
        print(e)
        driver.quit()

if __name__=='__main__':
    LoginMethodSwitch()
