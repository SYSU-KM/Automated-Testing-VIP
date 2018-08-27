import unittest2
import urllib
import urllib.request
import time
import os
import requests
from PIL import Image
import time
from PIL import ImageEnhance
import pytesseract

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class LoginError(Exception):
    pass


def LoginWithVC(username,password):
    global cnt
    driver=webdriver.Edge()
    url="https://passport.vip.com/login"
    driver.get(url)
    time.sleep(2)
    driver.maximize_window()

    #切换为账号登录
    driver.find_element_by_xpath("//div[@class='c-tab-nav']/div[2]").click()
    time.sleep(2)

    driver.find_element_by_id("J_login_name").send_keys(username)
    driver.find_element_by_id("J_login_pwd").send_keys(password)
    '''先点击一次登录才能确定是否需要验证码'''
    driver.find_element_by_id("J_login_submit").click()

    correct_account = "15989046165"
    correct_pwd = "VIPskm168"

    target = driver.find_element_by_id("J_login_code")

    '''如果需要验证码,先获取验证码'''
    if (target):
        print("Verification Cade Needed")
        driver.save_screenshot(r"D:\\VIP\\aa.png")  # 截取当前网页，该网页有我们需要的验证码
        imgelement = driver.find_element_by_xpath("//span[@class='u-code-img']/img")
        # imgelement = driver.find_element_by_id("code")  #定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽

        print("size : %r " % size)

        coderange = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                     int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标

        i = Image.open(r"D:\\VIP\\\aa.png")  # 打开截图
        frame4 = i.crop(coderange)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(r"D:\\VIP\\frame4.png")
        i2 = Image.open(r"D:\\VIP\\frame4.png")
        imgry = i2.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
        i3 = sharpness.enhance(3.0)  # 3.0为图像的饱和度
        i3.save("D:\\VIP\\image_code.png")
        i4 = Image.open("D:\\VIP\\image_code.png")
        VerificationCode = pytesseract.image_to_string(i2).strip()  # 使用image_to_string识别验证码
        print("VerificationCode: %r" % VerificationCode)

        '''填入验证码'''
        driver.find_element_by_id("J_login_code").send_keys(VerificationCode)

        try:
            driver.find_element_by_id("J_login_submit").click()
            time.sleep(1)

            current_url = driver.current_url
            # 登录成功
            if (current_url.find("www.vip.com")):
                # 账号，密码不同时不正确却能登录成功
                if (username != correct_account and password != correct_pwd):
                    raise LoginError("Failed! - Login Test Error")
                else:
                    print("Passed! - Login est Case %r" % cnt)
                    driver.get_screenshot_as_file("D:\\VIP\\Passed_Login_Test_Case_%r.png" % cnt)
                    cnt = cnt + 1
                    driver.quit()
            else:
                if (current_url.find("passport.vip.com")):
                    # 账号，密码不匹配，不能登录的情况
                    if (username != correct_account or password != correct_pwd):
                        print("Passed! - Login est Case %r" % cnt)
                        driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Test_Case_%r.png" % cnt)
                        cnt = cnt + 1
                        driver.quit()

                    # 账号，密码正确却不能登录
                    else:
                        print("Failed! - Login Test Case %r" % cnt)
                        driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Test_Case_%r.png" % cnt)
                        cnt = cnt + 1
                        driver.quit()

        except LoginError as e:
            print(e)

    #如果不需要验证码
    else:
        try:
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
            LoginWithVC(usr,pwd)