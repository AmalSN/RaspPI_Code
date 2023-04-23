from selenium import webdriver
import os
import time
import cv2

def extract_pic():
    url = "http://192.168.4.1/"

    dir = "./CameraImages"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))

    driver = webdriver.Firefox()
    driver.get(url)
    for i in range(50):
        driver.get_screenshot_as_file(dir+"/"+str(i)+".png")
        time.sleep(0.1)

    for f in os.listdir(dir):
        img = cv2.imread(os.path.join(dir,f))
        img = img[10:250,10:400]
        img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(os.path.join(dir,f),img)

extract_pic()