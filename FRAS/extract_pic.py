from selenium import webdriver
import os
import time

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


extract_pic()