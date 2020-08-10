#!C:\Users\Mohanapriya\AppData\Local\Programs\Python\Python37\python.exe
import cgi,os
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import pandas as pd
from spacy import displacy
from collections import Counter
import en_core_web_sm
from spacy.matcher import Matcher
import re


print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
pn=str(form.getvalue("outputtext"))
des=str(form.getvalue("outputtext1"))
pn_1=form.getvalue("out")
des_1=form.getvalue("out1")

fle=form['filename']

fn=os.path.basename(fle.filename)

fn="books/"+fn
i = 0
t = 0

t = 0
i = 0
l = ""


class Paragraphs:

    def __init__(self, fileobj, separator='\n'):

        # Ensure that we get a line-reading sequence in the best way possible:

        # Check if the file-like object has an xreadlines method
        self.seq = fileobj.readlines()

        self.line_num = 0  # current index into self.seq (line number)
        self.para_num = 0  # current index into self (paragraph number)

        # Ensure that separator string includes a line-end character at the end
        if separator[-1:] != '\n': separator += '\n'
        self.separator = separator

    def __getitem__(self, index):
        if index != self.para_num:
            raise TypeError("Only sequential access supported")
        self.para_num += 1
        # Start where we left off and skip 0+ separator lines
        while 1:
            # Propagate IndexError, if any, since we're finished if it occurs
            line = self.seq[self.line_num]
            self.line_num += 1
            if line != self.separator: break
        # Accumulate 1+ nonempty lines into result
        result = [line]
        while 1:
            # Intercept IndexError, since we have one last paragraph to return
            try:
                # Let's check if there's at least one more line in self.seq
                line = self.seq[self.line_num]
            except IndexError:
                # self.seq is finished, so we exit the loop
                break
            # Increment index into self.seq for next time
            self.line_num += 1
            if line == self.separator: break
            result.append(line)
        return ''.join(result)


# Here's an example function, showing how to use class Paragraphs:
pp = Paragraphs(open(fn))
pat="\\b("+pn+")(?:\\W+\\w+){1,6}?\\W+("+des+")\\b"
pat1="\\b("+des+")(?:\\W+\\w+){1,6}?\\W+("+pn+")\\b"
pattern = re.compile(pat,re.IGNORECASE)
pattern1 = re.compile(pat1,re.IGNORECASE)

nlp = spacy.load("en_core_web_sm")
ff = ""
for sentence in pp:

    doc_1 = nlp(sentence)

    if t == 1:
        for token in doc_1:
            if token.pos_ == 'PRON':
                ff += sentence
                t = 1
            else:
                t = 0

    if (pattern.search(str(sentence)) is not None) | (pattern1.search(str(sentence)) is not None):
        i = i + 1
        

        ff += l
        ff += sentence
        t = 1
    else:
        l = sentence

# defined entities

import random


def get_entity_options(random_colors=False):
    """ generating color options for visualizing the named entities """

    def color_generator(number_of_colors):
        color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(number_of_colors)]
        return color

    entities = ["LOCATION","ENTITY"]

    colors = dict(ENT="#E8DAEF")

    if random_colors:
        color = color_generator(len(entities))
        for i in range(len(entities)):
            colors[entities[i]] = color[i]
    else:
        entities_cat_1 = dict(LOCATION="#F9E79F")
        entities_cat_2 = dict(ENTITY="#82E0AA")

        entities_cats = [entities_cat_1, entities_cat_2]
        for item in entities_cats:
            colors = {**colors, **item}

    options = {"ents": entities, "colors": colors}
    print(options)
    return options


class EntityMatcher(object):
    name = "entity_matcher"

    def __init__(self, nlp, terms,terms1, label,label1):
        patterns = [nlp.make_doc(text) for text in terms]
        patterns1 = [nlp.make_doc(text) for text in terms1]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(label, None, *patterns)
        self.matcher.add(label1, None, *patterns1)

    def __call__(self, doc):
        matches = self.matcher(doc)
        seen_tokens = set()
        new_entities = []
        entities = doc.ents
        for match_id, start, end in matches:
            #Span(doc, start, end, label=match_id)
            # doc.ents = list(doc.ents) + [span]
            # check for end - 1 here because boundaries are inclusive
            if start not in seen_tokens and end - 1 not in seen_tokens:
                new_entities.append(Span(doc, start, end, label=match_id))
                entities = [
                    e for e in entities if not (e.start < end and e.end > start)
                ]
                seen_tokens.update(range(start, end))

        doc.ents = tuple(entities) + tuple(new_entities)
        return doc


nlp = spacy.load("en_core_web_sm")


t=pn_1.split()
t_1=[]
t_2=[]
for i in t:
    sc=i.swapcase()
    t_1.append(sc)
    sc1=i.title()
    t_2.append(sc1)

t_1.extend(t_2)
t.extend(t_1)
terms = t

label = 'LOCATION'
t1=des_1.split()
t_1=[]
t_2=[]
for i in t1:
    sc=i.swapcase()
    t_1.append(sc)
    sc1=i.title()
    t_2.append(sc1)

t_1.extend(t_2)
t1.extend(t_1)
terms1= t1

print(isinstance(terms1,tuple))
label1='ENTITY'
entity_matcher = EntityMatcher(nlp, terms,terms1,label,label1)

nlp.add_pipe(entity_matcher, after="ner")


dff=nlp(ff)
doc_ff = entity_matcher(dff)

final = ([(ent.text, ent.label_) for ent in doc_ff.ents])

from spacy import displacy
# displacy.serve(doc, style='ent')
df = pd.DataFrame(final)
df.to_excel('Custom_entity.xlsx')

opti = get_entity_options()

doc_ff.user_data["title"] = "Label:Location   "+pn+"    Entities:"+des

svg = displacy.render(doc_ff, style="ent", options=opti)

open("out.html", "w", encoding="utf-8").write(svg)


import subprocess
hh="localhost/natural/out.html"
bro="C:/Users/Mohanapriya/AppData/Local/Programs/Opera/launcher.exe"
subprocess.Popen([bro,hh])
