# coding:utf-8
from selenium import webdriver
from time import sleep
import unittest
from PIL import Image
from PIL import ImageEnhance
import pytesseract
driver=webdriver.Edge()
url="https://passport.baidu.com/?getpassindex"
driver.get(url)
driver.maximize_window()
driver.save_screenshot(r"E:\\aa.png")  #截取当前网页，该网页有我们需要的验证码
imgelement = driver.find_element_by_xpath(".//*[@id='forgotsel']/div/div[3]/img")
#imgelement = driver.find_element_by_id("code")  #定位验证码
location = imgelement.location  #获取验证码x,y轴坐标
size=imgelement.size  #获取验证码的长宽

print("size : %r " %size)

coderange=(int(location['x']),int(location['y']),int(location['x']+size['width']),
           int(location['y']+size['height'])) #写成我们需要截取的位置坐标

i=Image.open(r"E:\aa.png") #打开截图
frame4=i.crop(coderange)  #使用Image的crop函数，从截图中再次截取我们需要的区域
frame4.save(r"E:\frame4.png")
i2=Image.open(r"E:\frame4.png")
imgry = i2.convert('L')   #图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
sharpness =ImageEnhance.Contrast(imgry)#对比度增强
i3 = sharpness.enhance(3.0)  #3.0为图像的饱和度
i3.save("E:\\image_code.png")
i4=Image.open("E:\\image_code.png")
text=pytesseract.image_to_string(i2).strip() #使用image_to_string识别验证码
print (text)