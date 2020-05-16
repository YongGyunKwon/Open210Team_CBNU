from PIL import Image
from gtts import gTTS
from pdfminer.layout import LAParams
from pytesseract import *
import time
import pygame.mixer
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from io import StringIO
from io import open
from urllib.request import urlopen
import docx2txt

#OCR Tesseract 임시방편...
def image_to_string(filename):
    img=Image.open(filename)
    text=pytesseract.image_to_string(img,lang='kor+eng')
    print(text)
    return text

#text to speech function
def g_tts(text,file_name,file_type):
    tts=gTTS(text=text,lang='ko')
    save_as=file_name+'.'+file_type
    tts.save(save_as)


#play voice
def play_file(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(50)
    pygame.mixer.music.stop()


def read_pdf_file(pdfFile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdfFile)

    content=retstr.getvalue()
    retstr.close()
    return content


# pdf_file=open("__filename__","rb")
# contents=read_pdf_file(pdf_file)
# contents is text value.

def read_pdf_url(pdfurl):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfurl)

    content = retstr.getvalue()
    retstr.close()
    return content

#urlopen("urladress")


#docx_to_text
def read_docx_file(docxfile):
    text=docx2txt.process(docxfile)

    return text


