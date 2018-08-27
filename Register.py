import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class RegisterError(Exception):
    pass

def get_status(url):
    res=urllib.request.urlopen(url)
    page_status=res.getcode()
    return page_status

def Register():
    driver = webdriver.Edge()
    url = "https://passport.vip.com/login"
    driver.get(url)
    time.sleep(2)
    try:
        # 检测目标页面是否可达
        targetLink = "https://passport.vip.com/register"
        page_status = get_status(targetLink)

        if (page_status == 200):
            driver.find_element_by_class_name("c-register-link").click()
            time.sleep(2)

            # 等待页面渲染完成
            try:
                windows=driver.window_handles
                '''切换到新标签页打开的注册页面'''
                driver.switch_to_window(windows[1])
                current_url = driver.current_url

                # 检查是否跳转至正确的VIP注册官网
                if (current_url == "https://passport.vip.com/register"):
                    print("Passed! - Register Page Redirect Test")
                    driver.get_screenshot_as_file("D:\\VIP\\Passed_Register_Page_Redirect_Test.png")
                    time.sleep(1)
                    driver.switch_to_window(windows[0])
                    #driver.implicitly_wait(2)
                    time.sleep(2)
                    driver.quit()
                else:
                    raise RegisterError("Failed! - Register Page Redirect Test")

            except RegisterError as e:
                print(e)

        else:
            driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Page_Redirect.png")
            driver.quit()
            raise RegisterError("Failed - Redirect Link Error")

    except RegisterError as e:
        print(e)

if __name__=='__main__':
    Register()
