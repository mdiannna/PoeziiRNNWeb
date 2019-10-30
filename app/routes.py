from app import app
from flask import render_template, request, redirect, url_for, session, flash

from app.forms import PasteTextForm

from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
import re
import multiprocessing
import pandas as pd
import numpy as np
import pickle


MODEL_NAME_CLF = "PoeziiCLF2.model"
MODEL_NAME_W2V = "word2vecPoezii2.model"


def predict(text):

    model = Word2Vec.load(MODEL_NAME_W2V)

    with open(MODEL_NAME_CLF, 'rb') as handle:
        clf = pickle.load(handle)

    # # new_text_filename = "datasets/O_ramai.txt"
    # new_text_filename = "datasets/poezie.txt"
    # text_file = open(new_text_filename, 'r')
    # lines = text_file.read()

    lines = text
    add_words_to_vocab(model, lines)

    words = text_to_words(text)
    x = words_to_vec(model, words, size)


    X1 = np.empty((1, size, 100))

    words = text_to_words(lines)
    x = words_to_vec(model, words, size)
    X1[0] = x

    nsamples, nx, ny = X1.shape
    X3 = X1.reshape((nsamples,nx*ny))

    print(clf.predict(X3))
    return clf.predict(X3)


size = 90


def text_to_words(text):
    text = re.sub(r'\\n', ' ', text)
    text = re.sub(r'\n', ' ', text)
    text = text.replace("...", '')
    text = text.replace("…", '')
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('"', '')
    text = text.replace("'", '')
    text = text.replace("  ", ' ')
    # text = text.replace("-", '')
    text = text.replace("–", '')
    text = text.replace("?", '')
    text = text.replace(":", '')
    text = text.lower()
    words = text.replace('\\n', '').replace('"\n"', ' ').split(' ')
    print(words)
    return words


def words_to_vec(model, words, size=None):
    if size != None:
        words = words[:size]
    else:
        size = len(words)

    X = np.empty((size, 100))
    print("Shape of X:", X.shape)
    for idx, word in enumerate(words):
        X[idx] = model[word]
    return X

def add_words_to_vocab(model, text):
    words = text_to_words(text)
    # model.train(words, total_examples=model.corpus_count, epochs=30, report_delay=1)
    # model.train(words, total_examples=model.corpus_count, epochs=30, report_delay=1)
    model.build_vocab([words], update=True)
    model.train([words], total_examples=model.corpus_count, epochs=30, report_delay=1)
    # model.train([words])
    return model



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PasteTextForm()
    print(request)
    if(request.method == 'POST'):
        print('POST')
    # if form.validate_on_submit():
        text = form.text.data
        author = predict(text)
        return redirect(url_for('predict_author', author=author))
        
    return render_template('index.html')

@app.route('/predict-author')
def predict_author():
    author = request.args['author']
    return render_template('predict_author.html', author=author)

