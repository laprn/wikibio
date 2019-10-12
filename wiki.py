import requests
import wikiparser as wp
import json
import re

#wikiparser code
targetPerson = 'Werner Heisenberg'
targetPerson = re.sub(' ', '_', targetPerson)
targetPersonInfo = wp.infoBox('https://en.wikipedia.org/wiki/' + targetPerson)
image = wp.getMainImage('https://en.wikipedia.org/wiki/' + targetPerson)
targetPersonInfo['image'] = image['link']

with open(targetPerson + '.json', 'w') as f:
    json.dump(targetPersonInfo, f, indent=4)