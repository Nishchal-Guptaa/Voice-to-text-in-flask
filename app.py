from flask import render_template, Flask, jsonify
from tut2 import get_text as gt
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/voice', methods = ['GET','POST'])
def text():
    return f"{jsonify(gt())}Text recorded"

if __name__ == "__main__":
    app.run(debug=True)