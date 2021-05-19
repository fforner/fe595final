from flask import Flask
from flask import Flask, request, jsonify, render_template
from Polarity_and_Frequency import *
from simillarity import *
from subjectivity import *
import pandas as pd
from gensim.summarization import summarize
from pos_tagging import *
from word_cloud import *
import re
from matplotlib.figure import Figure
import random
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Response
from wiki_request import *
import matplotlib.pyplot as plt
import os
app = Flask(__name__)
def say_hello(username = "World"):
    return '<h1>FE 595 Final Term Project</h1>'

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>FE 595 Final Term Project</title> </head>\n<body><b>Project Members</b><br/><ul><li>Akshat Goel</li><li>Francesco Forner</li><li>Giovanni Scalzotto</li><li>Kevin Shah</li></ul>  '''
instructions = '''
    <p><a href="/services">Check out the NLP services!</a></p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'


def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

#To create plot for frequency
def create_figure(x,y):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = x
    ys = y
    axis.plot(xs, ys)
    return fig


def isValidURL(str):
    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if (re.search(p, str)):
        return True
    else:
        return False
@app.route('/services', methods=['POST', 'GET'])
def services():
    if request.method == 'POST':
        form_data = request.form

        if form_data['type'] == 'wiki_link':
            if isValidURL(form_data['wiki']):
                if form_data['typescraper'] == 'our_scraper':
                    form_text = scrape_wiki(form_data['wiki'])
                else:
                    form_text = scrape_wiki_package(form_data['wiki'])
            else:
                return '<html><p>Please enter a valid link</p></html>'
        else:
            form_text = form_data['content']

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        no_punct = ""
        for i in form_text:
            if i not in punctuations:
                no_punct = no_punct + i
        form_text = no_punct
        if form_data['service'] == 'polarity_and_frequency':
            pol_score = polarity(form_text)
            freq_results = frequency(form_text)
            x = [i[0] for i in freq_results]
            y = [i[1] for i in freq_results]
            return render_template('pol_and_freq.html', pol_score = pol_score, labels = x, values = y, max = max(y))
        elif form_data['service'] == 'similarity':
            word1sim, word2sim, word1, word2 = similarity(form_text,form_data['word1'],form_data['word2'])
            x = [i[1] for i in word1sim]
            y = [i[1] for i in word2sim]
            word1sim = pd.DataFrame(word1sim, columns = ['Word','Similarity score with ' + word1])
            word1sim = word1sim.sort_values(by=['Similarity score with '+ word1],ascending=False)
            word2sim = pd.DataFrame(word2sim, columns = ['Word','Similarity score with ' + word2])
            word2sim = word2sim.sort_values(by=['Similarity score with '+ word2], ascending=False)
            #return render_template('similarity.html', labels = x, values = y, max = 1)
            return render_template('similarity.html',table1=[word1sim.to_html(classes='data')], title1=word1sim.columns.values,table2=[word2sim.to_html(classes='data')], title2=word2sim.columns.values)
        elif form_data['service'] == 'word_cloud': #Akshat
            word_freqs, max_freq = word_cloud_generator(form_text)
            return render_template('word_cloud.html',word_freqs = word_freqs, max_freq = max_freq )
        elif form_data['service'] == 'pos_tagging':#Akshat
            from pathlib import Path
            desc = '<!DOCTYPE html><html lang="en"><body><table> <tr> <th>Type</th> <th>Description</th> </tr> <tr> <td>Person</td> <td>People, Including fictional</td> </tr> <tr> <td>NORP</td> <td>Nationalities or religious or political group</td> </tr> <tr> <td>Facility</td> <td>Buildings, Airports, Highways, Bridges, etc</td> </tr> <tr> <td>ORG</td> <td>Companies, Agencies, Institutions, etc</td> </tr> <tr> <td>GPE</td> <td>Countries, Cities, states</td> </tr> <tr> <td>LOC</td> <td>NON GPE locations, mountain ranges, bodies of water</td> </tr> <tr> <td>Product</td> <td>Objects, Vehicles, foods, etc</td> </tr> <tr> <td>Event</td> <td>Named hurricanes, battles, wars, sports events, etc</td> </tr> <tr> <td>Work_of_Art</td> <td>Titles of Books, songs, etc</td> </tr> <tr> <td>Law</td> <td>Named documents made into laws</td> </tr> <tr> <td>Language</td> <td>Any named language</td> </tr> <tr> <td>Date</td> <td>Absolute or relative dates or periods</td> </tr> <tr> <td>Time</td> <td>Times smaller than a day</td> </tr> <tr> <td>Percent</td> <td>Percentage, including %</td> </tr> <tr> <td>Money</td> <td>Monetary values, including unit</td> </tr> <tr> <td>Quantity</td> <td>Measurements, as of weight or distance</td> </tr> <tr> <td>Ordinal</td> <td>"first","second",etc</td> </tr> <tr> <td>Cardinal</td> <td>Numerals that do not fall under another type</td> </tr> <tr> <td></td> <td></td> </tr></table></body></html>'
            svg = pos_tagging(form_text)
            return '{} {}'.format(desc,svg)
        elif form_data['service'] == 'subjectivity': #Giovanni
            sub = subjectivity(form_text)
            return render_template('subjectivity.html', data1 = sub, content = form_data['content'])
        elif form_data['service'] == 'summarization':#Kevin
            valerr = None
            try:
                summary = summarize(form_text, ratio=0.2)
            except ValueError as e:
                valerr = str(e)
            if valerr != None:
                return render_template('summarizationerr.html', err = valerr)
            else:
                return render_template('summarization.html',data1 = summary, content = form_data['content'])
        elif form_data['service'] == 'all_services': #Akshat
            pol_score = polarity(form_text)
            freq_results = frequency(form_text)
            x = [i[0] for i in freq_results]
            y = [i[1] for i in freq_results]
            word1sim, word2sim, word1, word2 = similarity(form_text, form_data['word1'], form_data['word2'])
            word1sim = pd.DataFrame(word1sim, columns=['Word', 'Similarity score with ' + word1])
            word1sim = word1sim.sort_values(by=['Similarity score with ' + word1], ascending=False)
            word2sim = pd.DataFrame(word2sim, columns=['Word', 'Similarity score with ' + word2])
            word2sim = word2sim.sort_values(by=['Similarity score with ' + word2], ascending=False)
            word_freqs, max_freq = word_cloud_generator(form_text)
            sub = subjectivity(form_text)
            svg = pos_tagging(form_text)
            return render_template('all_services.html',pol_score = pol_score, labels = x, values = y, max = max(y),table1=[word1sim.to_html(classes='data')], title1=word1sim.columns.values,table2=[word2sim.to_html(classes='data')], title2=word2sim.columns.values,word_freqs = word_freqs, max_freq = max_freq , data1 = sub, content = form_data['content'],svg=svg[308:-16])

    if request.method == 'GET':
        return render_template("imput.html")

# add a rule for the index page.
app.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug = True)
