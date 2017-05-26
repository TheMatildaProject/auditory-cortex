#! /usr/bin/env python
import base64
import speech_to_text
from flask import Flask, jsonify, request

app = Flask(__name__) 

@app.route('/', methods=['POST'])
def api():
    if not request.json or not 'audio' in request.json:
        return jsonify({'error': 'Missing audio'}), 400

    stt = SpeechToText(base64.b64decode(request.json['audio']))
    text = stt.getFromGoogle()
    return jsonify({'text': text});

if __name__ == "__main__":
    app.run(debug=True)