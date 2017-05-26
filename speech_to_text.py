import speech_recognition as sr

class SpeechToText(object):
    def __init__(self, audio):
        self._audio = audio
 
    def getFromGoogle(self, text):
        r = sr.Recognizer()

        try:
            return r.recognize_google(self._audio)
        except sr.UnknownValueError:
            return ''
        except sr.RequestError as e:
            return null