import cv2
from pdf2image import convert_from_path, convert_from_bytes
import os
from subprocess import Popen,PIPE

def Image_Converter(filename):

    file = "Task8_2017038106.pdf"
    filepath = 'C:/Users/ygkwo/PycharmProjects/Open210Team_CBNU/Fuction/Task8_2017038106.pdf'
    conv = convert_from_bytes(open(filename, 'rb').read())

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
        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours

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


a= os.path.abspath('./tester.pdf')

Image_Converter(a)