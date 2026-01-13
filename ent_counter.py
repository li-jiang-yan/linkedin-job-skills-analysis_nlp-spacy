"""
Counts entity text occurrence from ent_filter_.spacy
"""
from collections import Counter
import json
from operator import attrgetter
import spacy
from spacy.tokens import DocBin

def text_lower(e):
    """Returns the lowercase of the given entity's text"""
    return e.text.lower()

def ent_texts(d):
    """Returns a set containing the text of entities in d"""
    return set(map(text_lower, d.ents))

nlp = spacy.load("en_core_web_lg")
doc_bin = DocBin().from_disk("ent_filter_.spacy")
docs = doc_bin.get_docs(nlp.vocab)
c = Counter()
for doc in docs:
    c.update(ent_texts(doc))
with open("ent_counter.json", "w", encoding="utf-8") as f:
    json.dump(c.most_common(), f, indent=4)
