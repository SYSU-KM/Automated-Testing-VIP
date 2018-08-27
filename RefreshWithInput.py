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
def RefreshWithInput():
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

    driver.get_screenshot_as_file("D:\\VIP\\Input_The_Account_And_Password.png")
    driver.refresh()
    time.sleep(1)
    driver.get_screenshot_as_file("D:\\VIP\\After_Refreshing_The_Page.png")
    driver.quit()

if __name__=='__main__':
    RefreshWithInput()