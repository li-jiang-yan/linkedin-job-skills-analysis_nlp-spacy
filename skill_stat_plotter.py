"""
Plot the occurrence of each skill picked up by spaCy
"""
import json
import matplotlib.pyplot as plt

def load_json(filename):
    """Returns data saved into a given path"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

SKILLS = ["Python", "SQL", "AI", "Java", "AWS", "API", "C++", "Linux", "Azure",
          "JavaScript", "DevOps", "PyTorch", "Docker", "GCP", "UI", "CI", "TensorFlow",
          "ETL", "Excel", "Tableau"]

divisor = len(load_json("scraper/job_descriptions.json"))
counters = dict(load_json("ent_counter.json"))
x = SKILLS[:12]
height = list(map(lambda k: counters[k] / divisor, x))

plt.bar(x, height)
plt.xlabel("Skill")
plt.ylabel("% of Computer Science job posts")
plt.title(f"Skills picked up by spaCy in {divisor} Computer Science job posts")
plt.show()
