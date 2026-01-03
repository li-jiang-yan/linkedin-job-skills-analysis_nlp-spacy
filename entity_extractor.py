"""
Extract all the entities from job_descriptions.json
"""
import json
from collections import Counter
from operator import attrgetter
from tqdm import tqdm
import spacy

def load_json():
    """Returns data saved into job_descriptions.json"""
    filename = "scraper/job_descriptions.json"
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def count_ents_text(ents_it):
    """Count each entity text in ents_sets"""
    c = Counter()
    for ents in tqdm(ents_it):
        ent_texts_set = set(map(attrgetter("text"), ents))
        c.update(ent_texts_set)
    return c

def save_json(input_dict):
    """Save a given input dict into entities.json"""
    filename = "entities.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(input_dict, f, indent=4)

nlp = spacy.load("en_core_web_lg")
data = load_json()
ents_iter = map(attrgetter("ents"), nlp.pipe(data))
counter = count_ents_text(ents_iter)
save_json(counter)
