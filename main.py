from gtts import gTTS
from playsound import playsound
from PIL import Image, ImageGrab
import pytesseract
import sys
import os

imageFileName = "image.png"
try:
    im = ImageGrab.grabclipboard()
    im.save(imageFileName,'PNG')
except AttributeError:
    sys.exit("no image in the clipboard!")
  
text = pytesseract.image_to_string(Image.open(imageFileName) )
filename = "sample.mp3"

lang='en'
tts = gTTS(text=text, lang=lang)
try:
    tts.save(filename)
except PermissionError:
    print('Permission denied! Remove the sample.mp3 file')
playsound(filename)
os.remove(filename)