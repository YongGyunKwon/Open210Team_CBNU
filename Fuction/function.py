from gtts import gTTS
import time
import pygame.mixer

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