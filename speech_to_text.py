#import speech_recognition as sr
import wave
import io
import io, os
from google.auth import environment_vars
from google.cloud import speech

class SpeechToText(object):
    def __init__(self, audio):
        self._audio = audio
        self._speech_client = speech.Client()
 
    def getFromGoogle(self):
        with io.BytesIO(self._audio) as audio_file:
            content = audio_file.read()
            sample = self._speech_client.sample(
                content,
                source_uri=None,
                encoding='LINEAR16')

        alternatives = sample.recognize('en-UK')

        for alternative in alternatives:
            return alternative.transcript