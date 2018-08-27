import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class LoginError(Exception):
    pass

def Login(username,password):
    global cnt
    driver = webdriver.Edge()
    url = "https://passport.vip.com/login"
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()

    correct_account="15989046165"
    correct_pwd="VIPskm168"

    try:
        #切换为账号登录
        driver.find_element_by_xpath("//div[@class='c-tab-nav']/div[2]").click()
        time.sleep(2)

        driver.find_element_by_id("J_login_name").send_keys(username)
        driver.find_element_by_id("J_login_pwd").send_keys(password)
        driver.find_element_by_id("J_login_submit").click()
        time.sleep(1)

        current_url=driver.current_url
        #登录成功
        if(current_url.find("www.vip.com")):
            #账号，密码不同时不正确却能登录成功
            if(username!=correct_account and password!=correct_pwd):
                raise LoginError("Failed! - Login Test Error")
            else:
                print("Passed! - Login est Case %r" %cnt)
                driver.get_screenshot_as_file("D:\\VIP\\Passed_Login_Test_Case_%r.png" %cnt)
                cnt=cnt+1
                driver.quit()
        else:
            if(current_url.find("passport.vip.com")):
                #账号，密码不匹配，不能登录的情况
                if(username!=correct_account or password!=correct_pwd):
                    print("Passed! - Login est Case %r" % cnt)
                    driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Test_Case_%r.png" % cnt)
                    cnt=cnt+1
                    driver.quit()

                #账号，密码正确却不能登录
                else:
                    print("Failed! - Login Test Case %r" %cnt)
                    driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Test_Case_%r.png" %cnt)
                    cnt=cnt+1
                    driver.quit()

    except LoginError as e:
        print(e)


if __name__=='__main__':

    username = ["15989046161",
                "15989046165",
                "15989046162"]

    password = ["VIPskm168"]

    cnt = 1
    for usr in username:
        for pwd in password:
            Login(usr,pwd)