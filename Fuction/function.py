from PIL import Image
from gtts import gTTS
from pytesseract import *
import time
import pygame.mixer


#OCR Tesseract 임시방편...
def image_to_string(filename):
    img=Image.open(filename)
    img.show()
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


