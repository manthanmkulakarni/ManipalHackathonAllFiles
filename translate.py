# -*- coding: utf-8 -*- 
from google.cloud import translate
import speech_recognition as sr
from gtts import gTTS 
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')

def translate_text(text,target='en'):
    """
    Target must be an ISO 639-1 language code.
    https://cloud.google.com/translate/docs/languages
    """
    translate_client = translate.Client()
    result = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))

    #mytext = u'ಆರೋಗ್ಯದ ಬಗ್ಗೆ ಗಮನ ಕೊಡು'
    mytext=result['translatedText']
    language = target
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("welcome"+target+".mp3")
    os.system("afplay welcome"+target+".mp3") 


example_text=r.recognize_google(audio)
#example_text=raw_input('enter the text\n')
#example_text ='''Hola saludos desde Colombia excelentes tutoriales me gustaría poder por lo menos tener los subtitulos ene español ...excelente gracias por compartir tus conocimientos'''
translate_text(example_text.decode('utf-8'),target='kn')
print("\n")
translate_text(example_text.decode('utf-8'),target='hi')




"""import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    print ('Done!')

text = r.recognize_google(audio, language = 'hi-IN')

print (text)

print (r.recognize_google(audio))"""