"""
Filters entities from j2docs.spacy
"""
from itertools import chain
from operator import attrgetter
import spacy
from spacy.tokens import DocBin

def from_disk(path):
    """Load a doc from a serialized DocBin from a file."""
    d_bin = DocBin().from_disk(path)
    return d_bin.get_docs(nlp.vocab)

def filter_ent(e):
    """Returns the given entity as passing the filter (True) or filtered (False)"""
    return e.text in texts

def filter_ents(d):
    """Returns a filtered iterable of the given doc's entities """
    d.set_ents(list(filter(filter_ent, d.ents)))
    return d

def ent_texts(d):
    """Returns an iterable containing the text of entities in d"""
    return map(attrgetter("text"), d.ents)

nlp = spacy.load("en_core_web_lg")
fdocs = from_disk("ent_filter.spacy")
texts = set(chain.from_iterable(map(ent_texts, fdocs)))
docs = from_disk("jd2docs.spacy")
doc_bin = DocBin(docs=map(filter_ents, docs), store_user_data=True)
doc_bin.to_disk("./ent_filter_.spacy")
