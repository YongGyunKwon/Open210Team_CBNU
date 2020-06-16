from PIL import Image
from gtts import gTTS
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pytesseract import pytesseract
import time
import pygame.mixer
#from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from io import StringIO
from io import open
from urllib.request import urlopen
import docx2txt
#from Fuction.ocr import *
from pdf2image import convert_from_path
import fitz
from pdf2image import convert_from_path, convert_from_bytes
import cv2
import numpy
import PyPDF2


#pdf to png converter
#pages is number of pages

#이거는 tessearct 설치하고 tesseract.exe 본인 컴퓨터 경로꺼로 설정
pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

#pdf파일을 png 파일로 변환하는 함수, 완성
def pdf2png(filename,pages):
    pdffile = filename
    doc = fitz.open(pdffile)
    for i in range(0,pages):
        page = doc.loadPage(4)  #number of page
        pix = page.getPixmap()

        output = "outfile"+str(i)+".jpg"
        pix.writePNG(output)



#pdf to image converter, 완성
def pdf2img_converter(filename):
    pages= convert_from_path(filename,500)

    for pages in pages:
        pages.save('out.jpg','JPEG')





#Image To String 1 ,이미지를 텍스트로 변환하는 함수, 완성, 이거 구동하기 위해 window tessearct 설치 해야한다
#이거는 톡방 링크에 있음
def image_to_string1(filename):
    img=Image.open(filename)

    #img2=Image.open(filename)
    #img2=deskew(img2)
    #img2=get_grayscale(img2)
    #img2=remove_noise(img2)

    text=pytesseract.image_to_string(img,lang='kor+eng')
    print(text)
    return text

#print(image_to_string1('11.PNG'))

#위에꺼랑 같은 기능인데
#이거로 실행해서 오류나기에 그냥 함수 두기만 할꺼다 (오버플로 떠서)
def image_to_string2(filename):
    img=cv2.imread(filename)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_result = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_result = cv2.medianBlur(img_result, 5)
    img_result = cv2.bilateralFilter(img_result, 9, 75, 75)

    text=pytesseract.image_to_string(img_result,lang='kor+eng')
    return text


#text to speech function 0
#위에서 텍스트로 변환한거를 음성으로 변환하는 함수
def g_tts(text,file_name,file_type):
    tts=gTTS(text=text,lang='ko')
    save_as=file_name+'.'+file_type
    tts.save(save_as)
    print("This is TTS")

#play voice 0
#변환된 음성파일 실행 근데 ui에 없어가지고 버튼 만들면 이거 쓰면됨
def play_file(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(50)
    pygame.mixer.music.stop()

'''
def pdfparser(data):

    fp = file(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()

    print(data)


pdfparser("tester.pdf")
'''

#영어만 추출 가능 , 한국어 추출 x

def read_pdf_file1(pdfFile):
    file=open(pdfFile,'rb')
    fileReader=PyPDF2.PdfFileReader(file)

    #fileReader.pageMode('utf-8')

    #fileReader.documentInfo
    #전체 페이지수 출력
    fulltext=""
    #print(fileReader.numPages)
    pagecounter=int(fileReader.numPages)
    for i in range(0,pagecounter):
        pageObj=fileReader.getPage(i)
        text=pageObj.extractText()
        #print(text)
        fulltext+=text

    return fulltext



#print(read_pdf_file1("./tester.pdf"))


def read_pdf_file(pdfFile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdfFile)

    content=retstr.getvalue()
    retstr.close()
    return content



#pdf url로도 열어지니까 일단 구현은 해놨는데
def read_pdf_url(pdfurl):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfurl)

    content = retstr.getvalue()
    retstr.close()
    return content


def read_docx_file(docxfile):
    text=docx2txt.process(docxfile)

    return text


