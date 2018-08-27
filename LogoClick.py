#coding=utf-8
import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep

def get_status(url):
    res=urllib.request.urlopen(url)
    page_status=res.getcode()
    return page_status

class logoRedirectError(Exception):
    pass

#登录页面跳转，登录界面左上角返回官网功能测试
def clickLogo():
    driver=webdriver.Edge()
    url="https://passport.vip.com/login"
    driver.get(url)
    time.sleep(2)
    try:
        #检测目标页面是否可达
        targetLink="https://www.vip.com/"
        page_status = get_status(targetLink)

        if(page_status==200):
            print("Passed! - Redirect to Login Page Test")
            driver.get_screenshot_as_file("D:\\VIP\\Passed_Login_Page_Redirect.png")
            driver.find_element_by_id("for-cascade-login-link").click()
            time.sleep(2)

            #等待页面渲染完成
            try:
                current_url=driver.current_url
                #检查是否跳转至正确的VIP官网
                if(current_url=="https://www.vip.com/"):
                    print("Passed! - Logo Redirect Test")
                    driver.get_screenshot_as_file("D:\\VIP\\Passed_Logo_Click_Test.png")
                else:
                    raise logoRedirectError("Failed! - Logo Redirect Test")

            except logoRedirectError as e:
                print(e)

        else:
            driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Page_Redirect.png")
            driver.quit()
            raise logoRedirectError("Failed - Redirect Link Error")

    except logoRedirectError as e:
        print(e)

if __name__=='__main__':
    clickLogo()