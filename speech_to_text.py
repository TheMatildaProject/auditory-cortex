#import speech_recognition as sr
import wave
import io
import os
import StringIO
from google.auth import environment_vars
from google.cloud import speech

class SpeechToText(object):
    def __init__(self, audio):
        file = open("file.wav","wb")
        file.write(audio) 
        file.close()

        #self._audio = wave.open("file.wav", "rb")
        #params = wav.getparams()
        #print params;
        #exit()
        #audio = sr.AudioData(, wav.getsamprate(), wav.getsampwidth())
        #self._audio = audio
        #self._tts = gTTS(text='Hello', lang='en', slow=True
        self._speech_client = speech.Client()
 
    def getFromGoogle(self):
        with io.open("file.wav", "rb") as audio_file:
            content = audio_file.read()
            sample = self._speech_client.sample(
                content,
                source_uri=None,
                encoding='LINEAR16')

        alternatives = sample.recognize('en-UK')

        for alternative in alternatives:
            return alternative.transcript

        #r = sr.Recognizer()

        #try:
         #   return r.recognize_google(self._audio)
        #except sr.UnknownValueError:
        #    return ''
        #except sr.RequestError as e:
        #    return null