"""
Convert all the job descriptions in job_descriptions.json to Doc objects
"""
import json
import spacy
from spacy.tokens import DocBin

def load_json():
    """Returns data saved into job_descriptions.json"""
    filename = "scraper/job_descriptions.json"
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

nlp = spacy.load("en_core_web_lg")
data = load_json()
doc_bin = DocBin(docs=nlp.pipe(data), store_user_data=True)
doc_bin.to_disk("./jd2docs.spacy")
