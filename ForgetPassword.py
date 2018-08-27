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

class ForgetPwdtError(Exception):
    pass

#登录页面跳转，登录界面左上角返回官网功能测试
def ForgetPwd():
    driver=webdriver.Edge()
    url="https://passport.vip.com/login"
    driver.get(url)
    time.sleep(2)
    try:
        #检测目标页面是否可达
        targetLink="https://safe.vip.com/login/findPW/page#step=1&pid="
        page_status = get_status(targetLink)

        if(page_status==200):
            #切换到账户登录
            driver.find_element_by_xpath("//div[@class='c-tab-nav']/div[2]").click()
            time.sleep(2)

            driver.find_element_by_class_name("i-forget-link").click()
            time.sleep(2)

            windows=driver.window_handles
            #切换到找回密码窗口
            driver.switch_to_window(windows[1])
            time.sleep(1)
            current_url1=driver.current_url
            if(current_url1==targetLink):
                print("Passed! - Redirect to Find Password Page Test")
                driver.get_screenshot_as_file("D:\\VIP\\Passed_Find_Password_Page_Redirect.png")
                driver.switch_to_window(windows[0])
                time.sleep(1)
                driver.quit()

            else:
                print("Failed! - Redirect to Find Password Page Test")
                raise ForgetPwdtError("Redirect to Find Password Page Test")

    except ForgetPwdtError as e:
        print(e)

if __name__=='__main__':
    ForgetPwd()