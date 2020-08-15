import requests
import wikiparser as wp
import json
import re
from fetch import targetPerson as targetPerson
import sys
from getBirthAndDied import getBirthAndDied

def appendInfo(targetPerson):
    with open('./person/{}.json'.format(targetPerson), 'r') as f:
        df = json.load(f)
    
    date = {'Born': '', 'Died': ''}
    for i in ['Born','Died']:
        try:
            date[i] = re.search(r'[0-9]{4}-[01]?[0-9]-[0-3]?[0-9]', df[i]).group()
        except:
            date[i] = getBirthAndDied(df[i])

    with open('bAndD.json', 'r') as f:
        df = json.load(f)

    df.append({'name':targetPerson, 'born':date['Born'], 'died':date['Died']})

    with open('bAndD.json', 'w') as f:
        json.dump(df, f, indent=4)

if __name__ == '__main__':
    appendInfo(targetPerson)