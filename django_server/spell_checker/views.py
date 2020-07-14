from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import TextForm

import pandas as pd
import pickle

import pythainlp

from pythainlp.corpus.common import thai_words
from pythainlp.tokenize import word_tokenize, DEFAULT_WORD_DICT_TRIE
from pythainlp.util import trie

from pythainlp import spell
from pythainlp.spell import NorvigSpellChecker

# Create your views here.

def index(request):
    text = "test"
    title = "MyClub Event Calendar - %s" % (text)
    return HttpResponse("<h1>%s</h1>" % title)

def spell_checker(request):
    # if this is a POST request we need to process the form data
    text = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TextForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            InputText = form.cleaned_data['InputText']

            dict_file = open("/root/geo_spellchecker/django_server/spell_checker/dataset/dict.pkl", "rb")
            geo_dictlist = pickle.load(dict_file)

            geo_spell_checker = NorvigSpellChecker(custom_dict=geo_dictlist,min_freq=5)
            allword_prob = geo_spell_checker.spell(InputText)
            #prob = geo_spell_checker.prob(test_text)
            predict_word = allword_prob[0]

            print("Input Text: "+InputText)
            print("Result Text: "+predict_word)

            text = predict_word

            # redirect to a new URL:
            return render(request, 'spell_checker_form.html', {'form': form, 'text': text}, )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TextForm()

    return render(request, 'spell_checker_form.html', {'form': form, 'text': text}, )