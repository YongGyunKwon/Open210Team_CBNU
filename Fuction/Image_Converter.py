import cv2
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes
import os
from subprocess import Popen,PIPE
import time
import matplotlib.pyplot as plt
import matplotlib.image as img
from pytesseract import pytesseract


def Image_Converter(filename):

    a = os.path.abspath(filename)

    file = "Task8_2017038106.pdf"
    filepath = 'C:/Users/ygkwo/PycharmProjects/Open210Team_CBNU/Fuction/Task8_2017038106.pdf'
    conv = convert_from_bytes(open(a, 'rb').read())

    i=1

    for con in conv:
        con.save('output'+str(i)+'.jpg', 'JPEG')
        i+=1

    for j in range(1,i):

        name1='output'+str(j)+'.jpg'
        image = cv2.imread(name1)  # pdf가 image 파일로 변환완료
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  # threshold
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        dilated = cv2.dilate(thresh, kernel, iterations=13)  # dilate
        im2, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours

        # for each contour found, draw a rectangle around it on original image
        for contour in contours:
            # get rectangle bounding contour
            [x, y, w, h] = cv2.boundingRect(contour)

            # discard areas that are too large
            if h > 300 and w > 300:
                continue

            # discard areas that are too small
            if h < 40 or w < 40:
                continue

            # draw rectangle around contour on original image
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)

        # write original image with added contours to disk
        cv2.imwrite(name1, image)  # image 파일에서 변환된 부분 plot 된 최종파일 출력

    b=os.path.abspath('output1.jpg')
    print(b)
    #im=cv2.imread(b,0)
    #print(im)
    #cv2.imshow('output1.jpg',im)
    c=img.imread('output1.jpg')
    print(c)
    plt.imshow(c)
    plt.show()
    time.sleep(1)

#a= os.path.abspath('./tester.pdf')

#Image_Converter(a)


def Image_Converter2(filename):

    a = os.path.abspath(filename)
    conv = convert_from_bytes(open(a, 'rb').read())
    i=1
    text1=""
    for con in conv:
        con.save('output'+str(i)+'.jpg', 'JPEG')
        a='output'+str(i)+'.jpg'
        img=Image.open('output')
        text2=pytesseract.image_to_string(img,lang='kor'+eng)
        text1.append(text2)
        i += 1

    print(text1)
    return text1


#Image_Converter2('tester.pdf')