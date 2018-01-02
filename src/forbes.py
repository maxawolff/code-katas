"""Python module to interact with a json file of the top 40 billionares."""
import json
import pdb


def json_to_dict(filename):
    """Open a json file and turn it into a dictionary."""
    doc = open(filename)
    jstring = doc.read()
    jdata = json.loads(jstring)
    return jdata


def billionaires():
    """Return info about the oldest billionaire who is under 80 and the youngest billionare."""
    bdata = json_to_dict('billionaires.json')
    youngest_valid_age = 100
    oldest_age_under_80 = 0
    youngest_billionare = 0
    oldest_billionare = 0
    for person in bdata:
        if person['age'] > oldest_age_under_80 and person['age'] < 80:
            oldest_age_under_80 = person['age']
            oldest_billionare = person['name']
        if person['age'] < youngest_valid_age and person['age'] > 0:
            youngest_valid_age = person['age']
            youngest_billionare = person['name']
    pdb.set_trace()
    # youngest_info = [youngest_billionare]
    # oldest_info = []