import pygame.mixer
import time
from PIL import Image
from pytesseract import *
from datetime import datetime
from Fuction.function import *
from UI import *




if __name__ =="__main__":
        text="hello"
        file_name="test"
        f_type="mp3"

        g_tts(text,file_name,f_type)

        play_file(file_name+'.'+f_type)

        print("hello")


