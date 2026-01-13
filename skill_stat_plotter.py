"""
Plot the occurrence of each skill picked up by spaCy
"""
import json
import matplotlib.pyplot as plt

def load_json(filename):
    """Returns data saved into a given path"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

SKILLS = ["python", "sql", "ai", "java", "aws", "api", "c++", "linux", "javascript",
          "azure", "devops", "pytorch", "docker", "gcp", "ui", "tensorflow", "ci",
          "etl", "excel", "tableau"]

divisor = len(load_json("scraper/job_descriptions.json"))
counters = dict(load_json("ent_counter.json"))
x = SKILLS[:12]
height = list(map(lambda k: counters[k] / divisor, x))

plt.bar(x, height)
plt.xlabel("Skill")
plt.ylabel("% of Computer Science job posts")
plt.title(f"Skills picked up by spaCy in {divisor} Computer Science job posts")
plt.show()
