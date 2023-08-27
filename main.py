"""
Slangify is a project for arabic slang translation.
Check out <https://github.com/SelimWaly/Slangify> for 
the original project.
"""
import time
import os
import sys
import io
from datetime import datetime
from langdetect import detect
from googletrans import Translator as google
initialized = False

lang = {
    "hello": "ازيك",
    "world": "كون",
    "how are you": "عامل ايه",
    "what's up": "خير",
    "whats up": "خير",
    "oh wow": "يا ديني",
    "oh my god": "يا ديني",
    "fuck": "احا",
    "shit": "خرا",
    "bitch": "ابن كلب",
    "sure": "اشطا",
    "okay": "تمام",
    "ok": "تمام",
    "damn": "يا حلاوة",
    "sexy": "مز",
    "idiot": "حمار",
    "stupid": "متخلف",
    "dumb": "عبيط",
    "chair": "كرسي",
    "couch": "كنبة",
    "table": "طربيظا",
    "computer": "كومبيوتر",
    "elevator": "اصانسير",
    "mouse": "فار",
}

def decode(raw):
    try:
        google_translate = google()
        detected_lang = google_translate.detect(raw).lang
        if detected_lang != 'en':
            translation = google_translate.translate(raw, src=detected_lang, dest='en')
            return translation.text
        else:
            return raw

    except Exception as e:
        return str(e)

class translator:
    """
    Interactable class for the Slangify module.
    Commands:
    .init() to initialize (must do)
    translate(text) to translate the text from any language to arabic slang (ar-sl - NEW)
    speak(text) to use text-to-speech in a voice specified for arabic slang (ar-sl - NEW)
    transcribe(file) to transcribe and look for any voice speaking in arabic slang (ar-sl - NEW) and return into normal text
    """
    def init():
        """Core function to initialize class"""
        global initialized
        initialized = True

    def translate(text: str = None):
        """Function to translate any language into arabic slang"""
        if initialized != True:
            raise Exception("[TRANSLATOR]: Slangify translator was never initialized\n    Hotfix: Initialize with translator.init()")
        else:
            if text == None:
                return None
            else:
                decode(raw=text)
                words = text.split()
    
    def speak(text: str = None):
        """Function to use text-to-speech using a voice specified for arabic slang"""
        if initialized != True:
            raise Exception("[TRANSLATOR]: Slangify translator was never initialized\n    Hotfix: Initialize with translator.init()")
        else:
            if text == None:
                return None
            else:
                decode(raw=text)
                words = text.split()

    def transcribe(file):
        """Function to use detect any arabic slang spoken in a file and return the text"""
            

            
