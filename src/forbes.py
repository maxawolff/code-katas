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
    youngest = 0
    oldest = 0
    for person in bdata:
        if person['age'] > oldest_age_under_80 and person['age'] < 80:
            oldest_age_under_80 = person['age']
            oldest = person
        if person['age'] < youngest_valid_age and person['age'] > 0:
            youngest_valid_age = person['age']
            youngest = person
    youngest_info = [youngest['name'],
                     youngest['net_worth (USD)'],
                     youngest['source']]
    oldest_info = [oldest['name'],
                   oldest['net_worth (USD)'],
                   oldest['source']]
    bill_info = {'Youngest Billionaire': youngest_info,
                 'Oldest Billionaire under 80': oldest_info}
    return bill_info
