#! /usr/bin/env python
import base64
from speech_to_text import SpeechToText
from flask import Flask, jsonify, request

app = Flask(__name__) 

@app.route('/', methods=['POST'])
def api():
    if not request.json:
        return jsonify({'error': 'Json header expected'}), 401

    if not 'audio' in request.json:
        return jsonify({'error': 'Missing audio'}), 400

    audio = request.json['audio']

    stt = SpeechToText(base64.b64decode(audio.encode())) # string to byte before decoding b64
    text = stt.getFromGoogle()
    return jsonify({'text': text});

if __name__ == "__main__":
    app.run(debug=True) 