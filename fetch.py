import requests
import wikipedia
import json
import re

targetPerson = 'George Berkeley'
targetPerson = re.sub(' ', '_', targetPerson)
def fetchBio(targetPerson):
    'fetch a basic information using wikiparser'

    targetPerson = re.sub(' ', '_', targetPerson)
    targetPersonInfo = wp.infoBox('https://en.wikipedia.org/wiki/' + targetPerson)
    image = wp.getMainImage('https://en.wikipedia.org/wiki/' + targetPerson)
    targetPersonInfo['image'] = image['link']

    with open('./person/{}.json'.format(targetPerson), 'w') as f:
        json.dump(targetPersonInfo, f, indent=4)


if __name__ == '__main__':
    fetchBio(targetPerson)
