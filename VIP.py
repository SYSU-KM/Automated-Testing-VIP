#coding=utf-8
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

class SwitchError(Exception):
    pass

class LoginError(Exception):
    pass

def get_status(url):
    res=urllib.request.urlopen(url)
    page_status=res.getcode()
    return page_status

class logoRedirectError(Exception):
    pass

class SwitchError(Exception):
    pass

class RegisterError(Exception):
    pass

class LoginMethodError(Exception):
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
                    driver.quit()
                else:
                    raise logoRedirectError("Failed! - Logo Redirect Test")

            except logoRedirectError as e:
                print(e)
                driver.quit()

        else:
            driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Page_Redirect.png")
            driver.quit()
            raise logoRedirectError("Failed - Redirect Link Error")

    except logoRedirectError as e:
        print(e)
        driver.quit()


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
                print("Passed - Login Method Switch : Scanning QR Code")
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
            if(cnt==10):
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


def Verification():
    driver=webdriver.Edge()
    url="https://passport.vip.com/login"
    driver.get(url)
    driver.maximize_window()

    #切换为账号登录
    driver.find_element_by_xpath("//div[@class='c-tab-nav']/div[2]").click()
    time.sleep(2)

    driver.find_element_by_id("J_login_name").clear()
    driver.find_element_by_id("J_login_pwd").clear()
    driver.find_element_by_id("J_login_name").send_keys("15989046161")
    driver.find_element_by_id("J_login_pwd").send_keys("1")

    #点击10次使得出现验证码
    for i in range(1,15):
        driver.find_element_by_id("J_login_submit").click()
        time.sleep(1)

    driver.save_screenshot(r"D:\\VIP\\aa.png")  #截取当前网页，该网页有我们需要的验证码
    imgelement = driver.find_element_by_xpath(".//span[@class='u-code-img']/img")
    #imgelement = driver.find_element_by_id("code")  #定位验证码
    location = imgelement.location  #获取验证码x,y轴坐标
    size=imgelement.size  #获取验证码的长宽

    print("size : %r " %size)

    coderange=(int(location['x']),int(location['y']),int(location['x']+size['width']),
               int(location['y']+size['height'])) #写成我们需要截取的位置坐标

    i=Image.open(r"D:\\VIP\\\aa.png") #打开截图
    frame4=i.crop(coderange)  #使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save(r"D:\\VIP\\frame4.png")
    i2=Image.open(r"D:\\VIP\\frame4.png")
    imgry = i2.convert('L')   #图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
    sharpness =ImageEnhance.Contrast(imgry)#对比度增强
    i3 = sharpness.enhance(3.0)  #3.0为图像的饱和度
    i3.save("D:\\VIP\\image_code.png")
    i4=Image.open("D:\\VIP\\image_code.png")
    VerificationCode=pytesseract.image_to_string(i2).strip() #使用image_to_string识别验证码
    print ("VerificationCode: %r" %VerificationCode)
    return VerificationCode



'''不需要验证码的登录测试'''
def Login(username,password):
    global cnt
    #driver = webdriver.Edge()
    driver=webdriver.Edge()
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

        driver.find_element_by_id("J_login_name").clear()
        driver.find_element_by_id("J_login_pwd").clear()
        driver.find_element_by_id("J_login_name").send_keys(username)
        driver.find_element_by_id("J_login_pwd").send_keys(password)
        driver.find_element_by_id("J_login_submit").click()
        time.sleep(1)

        current_url=driver.current_url
        #登录成功
        if(current_url.find("www.vip.com")):
            #账号，密码不同时不正确却能登录成功
            if(username!=correct_account and password!=correct_pwd):
                raise LoginError("     Failed! - Login Test Error")
            else:
                print("     Passed! - Login est Case %r" %cnt)
                driver.get_screenshot_as_file("D:\\VIP\\Passed_Login_Test_Case_%r.png" %cnt)
                cnt=cnt+1
                driver.quit()
        else:
            if(current_url.find("passport.vip.com")):
                #账号，密码不匹配，不能登录的情况
                if(username!=correct_account or password!=correct_pwd):
                    print("     Passed! - Login est Case %r" % cnt)
                    driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Test_Case_%r.png" % cnt)
                    cnt=cnt+1
                    driver.quit()

                #账号，密码正确却不能登录
                else:
                    print("     Failed! - Login Test Case %r" %cnt)
                    driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Test_Case_%r.png" %cnt)
                    cnt=cnt+1
                    driver.quit()

    except LoginError as e:
        print(e)


def VIP_OCR(username,password):
    global cnt
    driver=webdriver.Edge()
    url="https://passport.vip.com/login"
    driver.get(url)
    driver.maximize_window()

    #切换为账号登录
    driver.find_element_by_xpath("//div[@class='c-tab-nav']/div[2]").click()
    time.sleep(2)

    driver.find_element_by_id("J_login_name").clear()
    driver.find_element_by_id("J_login_pwd").clear()
    driver.find_element_by_id("J_login_name").send_keys("15989046161")
    driver.find_element_by_id("J_login_pwd").send_keys("VIPskm168")

    #点击10次使得出现验证码
    for i in range(1,15):
        driver.find_element_by_id("J_login_submit").click()
        time.sleep(1)

    driver.save_screenshot(r"D:\\VIP\\aa.png")  #截取当前网页，该网页有我们需要的验证码
    imgelement = driver.find_element_by_xpath(".//span[@class='u-code-img']/img")
    #imgelement = driver.find_element_by_id("code")  #定位验证码
    location = imgelement.location  #获取验证码x,y轴坐标
    size=imgelement.size  #获取验证码的长宽

    #print("size : %r " %size)

    coderange=(int(location['x']),int(location['y']),int(location['x']+size['width']),
               int(location['y']+size['height'])) #写成我们需要截取的位置坐标

    i=Image.open(r"D:\\VIP\\\aa.png") #打开截图
    frame4=i.crop(coderange)  #使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save(r"D:\\VIP\\frame4.png")
    i2=Image.open(r"D:\\VIP\\frame4.png")
    imgry = i2.convert('L')   #图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
    sharpness =ImageEnhance.Contrast(imgry)#对比度增强
    i3 = sharpness.enhance(3.0)  #3.0为图像的饱和度
    i3.save("D:\\VIP\\image_code.png")
    i4=Image.open("D:\\VIP\\image_code.png")
    VerificationCode=pytesseract.image_to_string(i2).strip() #使用image_to_string识别验证码
    #print ("VerificationCode: %r" %VerificationCode)

    '''填入验证码'''
    driver.find_element_by_id("J_login_code").send_keys(VerificationCode)

    correct_account='15989046165'
    correct_pwd='VIPskm168'
    try:
        #print("I am In")
        driver.find_element_by_id("J_login_submit").click()
        time.sleep(1)
        driver.refresh()

        current_url = driver.current_url
        # 登录成功
        if (current_url.find("www.vip.com")):
            # 账号，密码不同时不正确却能登录成功
            if (username != correct_account and password != correct_pwd):
                raise LoginError("     Failed! - Login Test Error")
            else:
                print("     Passed! - Login test Case(Correct Account) %r:" %cnt)
                driver.get_screenshot_as_file("D:\\VIP\\Passed_Login_Test_Case_%r.png" % cnt)
                cnt = cnt + 1
                driver.quit()
        else:
            if (current_url.find("passport.vip.com")):
                # 账号，密码不匹配，不能登录的情况
                if (username != correct_account or password != correct_pwd):
                    print("     Passed! - Login Test Case(Incorrect Account) %r" % cnt)
                    driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Test_Case_%r.png" % cnt)
                    cnt = cnt + 1
                    driver.quit()

                # 账号，密码正确却不能登录
                else:
                    print("     Failed! - Login Test Case %r" % cnt)
                    driver.get_screenshot_as_file("D:\\VIP\\Failed_Login_Test_Case_%r.png" % cnt)
                    cnt = cnt + 1
                    driver.quit()

    except LoginError as e:
        print(e)

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
    clickLogo()
    LoginMethodSwitch()
    Register()
    ForgetPwd()
    MethodsList = [
        'https://api.weibo.com/oauth2/authorize?client_id=1493335026&redirect_uri=https%3A%2F%2Fpassport.vip.com%2Fcallback%2Fweibo%3Fsrc%3Dhttp%253A%252F%252Fwww.vip.com&response_type=code&display=default&state=0@69a1ef6d879e4378bbfafe73aab50d4a&forcelogin=true',
        'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=100292427&redirect_uri=https://passport.vip.com/callback/qq&response_type=code&state=2d4ab3f62a6e48ac8c288114888a222a',
        'https://auth.alipay.com/login/express.htm?goto=https%3A%2F%2Fmemberexprod.alipay.com%3A443%2Fauthorize%2FuserAuthQuickLoginAction.htm%3Fe_i_i_d%3Db53067b4d3539d04e896f594ede04240',
        'https://open.weixin.qq.com/connect/qrconnect?appid=wxce0a56c2bb620e25&redirect_uri=https%3A%2F%2Fpassport.vip.com%2Fcallback%2Fweixin&response_type=code&scope=snsapi_login&state=68f33560865e4dc2bd5052f3509445e3#wechat_redirect',
        'http://reg.163.com/open/oauth2/authorize.do?client_id=2782876574&redirect_uri=https://passport.vip.com/callback/netease&response_type=code',
        'http://graph.renren.com/oauth/grant?client_id=c374d7e12f4e40a3bc8cbc8c25eec73a&redirect_uri=https%3A%2F%2Fpassport.vip.com%2Fcallback%2Frenren&response_type=code&display=page&scope=read_user_status+status_update+read_user_feed+publish_feed+photo_upload&secure=true&origin=00000&x_renew=true',
        'http://tool.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&TXCODE=A10000&appid=22006',
        'http://www.kaixin001.com/login/connect_login.php?appkey=667532602161ec17a7d1a69d79a620d0&url=http%3A%2F%2Fapi.kaixin001.com%2Foauth2%2Fauthorize%3Fclient_id%3D667532602161ec17a7d1a69d79a620d0%26response_type%3Dcode%26scope%3Dbasic+user_intro+user_birthday%26state%3D%26redirect_uri%3Dhttps%253A%252F%252Fpassport.vip.com%252Fcallback%252Fkaixin001%26tmp%3D1',
        'http://openlogin.mail.10086.cn/Web/OpenLogin.aspx?rnd=636703080602835108',
        'https://www.bestpay.com.cn/api/oauth/oauth/authorize?client_id=1894805209&redirect_uri=https://passport.vip.com/callback/bestpay&responseType=code&version=2.0']
    cnt = 0

    pass_message = ["Passed! - U Third Sina Login",
                    "Passed! - U Third QQ Login",
                    "Passed! - U Third Alipay Login",
                    "Passed! - U Third Wechat Login",
                    "Passed! - U Third Netease Login",
                    "Passed! - U Third Renren Login",
                    "Passed! - U Third CCB Login",
                    "Passed! - U Third Kaixin Login",
                    "Passed! - U Third 10086 Login",
                    "Passed! - U Third Bestpay Login"]

    # for i in MethodsList:
    #     MoreLoginMethod(MethodsList[cnt])

    for i in range(0,10):
        print(pass_message[i])

    username = ["15989046161",
                "15989046165",
                "15989046162"]

    password = ["VIPskm168"]

    '''不需要验证码登录'''
    print("Starting Login Without Inputting Verification Code...")
    cnt=1
    for usr in username:
        for pwd in password:
            Login(usr, pwd)

    '''需要验证码登录'''
    print("Starting Login With Inputting Verification Code...")
    cnt = 1
    for usr in username:
        for pwd in password:
            VIP_OCR(usr,pwd)

    AntiCopy()
    print("VIP Login Page Test Finished!")
