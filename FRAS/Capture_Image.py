import csv

import requests
import cv2
import os

import os.path

from extract_pic import extract_pic
# counting the numbers


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False



# Take image function

def takeImages():


    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    if(is_number(Id) and name.isalpha()):
        # cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        extract_pic()

        all_images = []

        folder_dir = os.getcwd() + '/' + 'CameraImages'

        for images in os.listdir(folder_dir):
            if (images is not None):

                # print(images)
                img = os.path.join(folder_dir, images)
                all_images.append(img)

        print(len(all_images))

        # cv2.imshow("image" ,all_images[0])

        # cv2.waitKey(5000)


        while(True):
            # ret, img = cam.read()

            print(sampleNum)
            img = cv2.imread(all_images[sampleNum])

            # cv2.imshow("image", img)
            
                    
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # faces = detector.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=1, minSize=(100,100), flags = cv2.CASCADE_SCALE_IMAGE)


            # for(x,y,w,h) in faces:

            # print("in loop")
            # cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
            #incrementing sample number
            #saving the captured face in the dataset folder TrainingImage
            cv2.imwrite("TrainingImage" + os.sep +name + "."+Id + '.' +
                        str(sampleNum) + ".jpg", gray)
            #display the frame
            cv2.imshow('frame', img)

            
            sampleNum = sampleNum+1
            #wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is more than 100
            elif sampleNum > 49:
                break
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        header=["Id", "Name"]
        row = [Id, name]

        requests.post("http://",params={"name":name,"rollNo":Id})

        if(os.path.isfile("StudentDetails"+os.sep+"StudentDetails.csv")):
            with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(j for j in row)
            csvFile.close()
        else:
            with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(i for i in header)
                writer.writerow(j for j in row)
            csvFile.close()
    else:
        if(is_number(Id)):
            print("Enter Alphabetical Name")
        if(name.isalpha()):
            print("Enter Numeric ID")
