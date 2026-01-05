"""
Filters entities from j2docs.spacy
"""
import json
import pandas as pd
import spacy
from spacy.tokens import DocBin

def load_orgs():
    """Returns a set of all organizations in orgs.json"""
    filename = "scraper/orgs.json"
    with open(filename, "r", encoding="utf-8") as f:
        return set(json.load(f))

def load_languages():
    """Returns a set of all the languages in language-codes/data/language-codes.csv"""
    df = pd.read_csv("language-codes/data/language-codes.csv")
    return set(df["English"])

orgs = load_orgs()
languages = load_languages()

def from_disk(path):
    """Load a doc from a serialized DocBin from a file."""
    d_bin = DocBin().from_disk(path)
    return d_bin.get_docs(nlp.vocab)

def filter_ent(e):
    """Returns the given entity as passing the filter (True) or filtered (False)"""
    # Filter entities based on labels_
    nskill_labels = ["CARDINAL", "DATE", "EVENT", "FAC", "GPE", "LAW", "LOC", "MONEY",
                     "NORP", "ORDINAL", "PERCENT", "PERSON", "QUANTITY", "TIME",
                     "WORK_OF_ART"]
    if (e.label_ in nskill_labels) or (e.text in orgs | languages):
        return False

    # Filter out entities with non-ASCII characters
    if not e.text.isascii():
        return False

    # Filter out entities with newlines
    if "\n" in e.text:
        return False

    # Filter out entities with commas
    if "," in e.text:
        return False

    return True

def filter_ents(d):
    """Returns a filtered iterable of the given doc's entities """
    d.set_ents(list(filter(filter_ent, d.ents)))
    return d

nlp = spacy.load("en_core_web_lg")
docs = from_disk("jd2docs.spacy")
doc_bin = DocBin(docs=map(filter_ents, docs), store_user_data=True)
doc_bin.to_disk("./ent_filter.spacy")
