from machinetranslation.translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route('/englishToFrench/<english_text>', methods=['GET'])
def translate_english_to_french(english_text):
    french_text = english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish/<french_text>', methods=['GET'])
def translate_french_to_english(french_text):
    english_text = french_to_english(french_text)
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
