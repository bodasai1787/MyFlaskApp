from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)




@app.route("/")
def home(): 
    return render_template('index.html')


@app.route("/analysis")
def analysis():
    return render_template('textAnalyzer.html')

def getCharceterCount(text):
    return len(text)

def getWordCount(text):
    return text.count(' ')-1

def getSentenceCount(text):
    return text.count('.')

def getParagraphCount(text):
    return text.count('\n')+1

@app.route("/text-analyzer", methods=['POST'])
def analyzeText():
    text = request.form['text-to-analyze']
    charecters = getCharceterCount(text)
    words = getWordCount(text)
    sentences = getSentenceCount(text)
    paragraphs = getParagraphCount(text)
    statData={
        'charecters' : charecters,
        'words' : words,
        'sentences' : sentences,
        'paragraphs' : paragraphs
    }
    return statData