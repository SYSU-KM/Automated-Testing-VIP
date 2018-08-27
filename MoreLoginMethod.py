#coding=utf-8
import unittest2
import urllib
import urllib.request
import time
import os
import requests

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class LoginMethodError(Exception):
    pass

def get_status(url):
    res=urllib.request.urlopen(url)
    page_status=res.getcode()
    return page_status

def MoreLoginMethod(targetURL):
    driver = webdriver.Edge()
    url = "https://passport.vip.com/login"
    driver.get(url)
    time.sleep(2)
    global cnt

    key_words=["api.weibo.com",
               "graph.qq.com",
               "auth.alipay.com",
               "open.weixin.qq.com",
               "reg.163.com",
               "graph.renren.com",
               "tool.ccb.com",
               "www.kaixin001.com",
               "openlogin.mail.10086.cn",
               "www.bestpay.com.cn"]

    pass_message=["Passed! - U Third Sina Login",
                  "Passed! - U Third QQ Login",
                  "Passed! - U Third Alipay Login",
                  "Passed! - U Third Wechat Login",
                  "Passed! - U Third Netease Login",
                  "Passed! - U Third Renren Login",
                  "Passed! - U Third CCB Login",
                  "Passed! - U Third Kaixin Login",
                  "Passed! - U Third 10086 Login",
                  "Passed! - U Third Bestpay Login"]

    fail_message=["Failed! - U Third Sina Login",
                  "Failed! - U Third QQ Login",
                  "Failed! - U Third Alipay Login",
                  "Failed! - U Third Wechat Login",
                  "Failed! - U Third Netease Login",
                  "Failed! - U Third Renren Login",
                  "Failed! - U Third CCB Login",
                  "Failed! - U Third Kaixin Login",
                  "Failed! - U Third 10086 Login",
                  "Failed! - U Third Bestpay Login"]

    Image_words=["Sina",
                  "QQ",
                  "Alipay",
                  "Wechat",
                  "Netease",
                  "Renren",
                  "CCB",
                  "Kaixin",
                  "10086",
                  "Bestpay"]

    try:
        if(cnt==0):
            print("Starting Login By Third Party Platform Account Test:")
            driver.find_element_by_class_name("u-third-sina").click()
        elif(cnt == 1):
            driver.find_element_by_class_name("u-third-qq").click()
        elif(cnt == 2):
            driver.find_element_by_class_name("u-third-alipay").click()
        elif(cnt == 3):
            driver.find_element_by_class_name("u-third-wechat").click()

        #-----------------------------------------------------------------
        elif(cnt == 4):
            driver.find_element_by_id("J_more_third_control").click()
            driver.implicitly_wait(2)
            driver.find_element_by_class_name("c-login-third-item c-login-third-item-1").click()
        elif(cnt == 5):
            driver.find_element_by_id("J_more_third_control").click()
            driver.implicitly_wait(2)
            driver.find_element_by_class_name("c-login-third-item c-login-third-item-2").click()
        elif(cnt == 6):
            driver.find_element_by_id("J_more_third_control").click()
            driver.implicitly_wait(2)
            driver.find_element_by_class_name("c-login-third-item c-login-third-item-3").click()
        elif(cnt == 7):
            driver.find_element_by_id("J_more_third_control").click()
            driver.implicitly_wait(2)
            driver.find_element_by_class_name("c-login-third-item c-login-third-item-4").click()
        elif(cnt == 8):
            driver.find_element_by_id("J_more_third_control").click()
            driver.implicitly_wait(2)
            driver.find_element_by_class_name("c-login-third-item c-login-third-item-5").click()
        elif(cnt == 9):
            driver.find_element_by_id("J_more_third_control").click()
            driver.implicitly_wait(2)
            driver.find_element_by_xpath("//ul[@class='c-login-third-list']/li[6]").click()

        time.sleep(1)
        windows=driver.window_handles
        driver.switch_to_window(windows[1])
        time.sleep(1)
        current_url=driver.current_url
        if(current_url.find(key_words[cnt])):
            print("     %r" %pass_message[cnt])
            driver.get_screenshot_as_file("D:\\VIP\\Passed_U_Third_%r.png" %Image_words[cnt])
            cnt=cnt+1
            driver.switch_to_window(windows[0])
            time.sleep(1)
            driver.quit()
            if(cnt==9):
                print("Third Party Platform Account Login Test Finished")
        else:
            driver.get_screenshot_as_file("D:\\VIP\\Failed_U_Third_%r.png" %Image_words[cnt])
            print("     %r" %fail_message[cnt])
            cnt=cnt+1
            driver.switch_to_window(windows[0])
            time.sleep(1)
            driver.quit()
            raise LoginMethodError(fail_message[cnt-1])

    except LoginMethodError as e:
        print(e)




if __name__ == '__main__':

    MethodsList=['https://api.weibo.com/oauth2/authorize?client_id=1493335026&redirect_uri=https%3A%2F%2Fpassport.vip.com%2Fcallback%2Fweibo%3Fsrc%3Dhttp%253A%252F%252Fwww.vip.com&response_type=code&display=default&state=0@69a1ef6d879e4378bbfafe73aab50d4a&forcelogin=true',
                 'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=100292427&redirect_uri=https://passport.vip.com/callback/qq&response_type=code&state=2d4ab3f62a6e48ac8c288114888a222a',
                 'https://auth.alipay.com/login/express.htm?goto=https%3A%2F%2Fmemberexprod.alipay.com%3A443%2Fauthorize%2FuserAuthQuickLoginAction.htm%3Fe_i_i_d%3Db53067b4d3539d04e896f594ede04240',
                 'https://open.weixin.qq.com/connect/qrconnect?appid=wxce0a56c2bb620e25&redirect_uri=https%3A%2F%2Fpassport.vip.com%2Fcallback%2Fweixin&response_type=code&scope=snsapi_login&state=68f33560865e4dc2bd5052f3509445e3#wechat_redirect',
                 'http://reg.163.com/open/oauth2/authorize.do?client_id=2782876574&redirect_uri=https://passport.vip.com/callback/netease&response_type=code',
                 'http://graph.renren.com/oauth/grant?client_id=c374d7e12f4e40a3bc8cbc8c25eec73a&redirect_uri=https%3A%2F%2Fpassport.vip.com%2Fcallback%2Frenren&response_type=code&display=page&scope=read_user_status+status_update+read_user_feed+publish_feed+photo_upload&secure=true&origin=00000&x_renew=true',
                 'http://tool.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&TXCODE=A10000&appid=22006',
                 'http://www.kaixin001.com/login/connect_login.php?appkey=667532602161ec17a7d1a69d79a620d0&url=http%3A%2F%2Fapi.kaixin001.com%2Foauth2%2Fauthorize%3Fclient_id%3D667532602161ec17a7d1a69d79a620d0%26response_type%3Dcode%26scope%3Dbasic+user_intro+user_birthday%26state%3D%26redirect_uri%3Dhttps%253A%252F%252Fpassport.vip.com%252Fcallback%252Fkaixin001%26tmp%3D1',
                 'http://openlogin.mail.10086.cn/Web/OpenLogin.aspx?rnd=636703080602835108',
                 'https://www.bestpay.com.cn/api/oauth/oauth/authorize?client_id=1894805209&redirect_uri=https://passport.vip.com/callback/bestpay&responseType=code&version=2.0']
    cnt=0
    for i in MethodsList:
        MoreLoginMethod(MethodsList[cnt])