from bs4 import BeautifulSoup
import os
import time
import requests

def extract_pic():
    url = "http://localhost:5500/site.html"

    html_content = requests.get(url).text
    dir = "./CameraImages"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))

    soup = BeautifulSoup(html_content, "html.parser")

    response = []
    for i in range(50):
        response.append(requests.get(soup.find("img")["src"]))
        time.sleep(0.1)

    for i,res in enumerate(response):
        with open(dir+"/"+str(i)+".png","wb") as file:
            file.write(res.content)
