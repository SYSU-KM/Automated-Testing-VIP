#coding=utf-8
import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep


#登录页面跳转，登录界面左上角返回官网功能测试
def AntiCopy():
    driver=webdriver.Edge()
    url="https://passport.vip.com/login"
    driver.get(url)
    time.sleep(2)

    driver.find_element_by_xpath("//div[@class='c-tab-nav']/div[2]").click()
    time.sleep(2)

    driver.find_element_by_id("J_login_name").clear()
    driver.find_element_by_id("J_login_pwd").clear()
    driver.find_element_by_id("J_login_name").send_keys("15989046165")
    driver.find_element_by_id("J_login_pwd").send_keys("12345")

    text=input("Copy the password from the website and make it as input: ")
    if(text=="12345"):
        print("Failed! - Anti-Copy Mechanism Test")
        driver.get_screenshot_as_file("D:\\VIP\\Failed_Anti_Copy_Mechanism.png")
        driver.quit()
    else:
        print("Passed! - Anti-Copy Mechanism Test")
        driver.get_screenshot_as_file("D:\\VIP\\Passed_Anti_Copy_Mechanism.png")
        driver.quit()

if __name__=='__main__':
    AntiCopy()