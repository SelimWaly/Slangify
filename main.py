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
}

def transcribe(raw):
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
    def init():
        global initialized
        initialized = True

    def translate(text):
        if initialized != True:
            raise Exception("[TRANSLATOR]: Slangify translator was never initialized\n    Hotfix: Initialize with translator.init()")
        else:
            transcribe(raw=text)
            

            
