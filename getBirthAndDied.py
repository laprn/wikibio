import re
from month import *

def getBirthAndDied(date):
    date = date.split()
    dateYear = [s for s in date if re.match(r'[0-9]{4}', s)][0]
    dateDate = [s for s in date if re.match(r'[0-9]{1,2}', s)][0].replace(',', '')
    if len(dateDate) == 1:
        dateDate = '0' + dateDate
    # for key in month:
    #     if key in birth:
    #         birthMonth = month[key]
    # the commented program is same as the bottom one
    dateMonth = [month[s] for s in month if s in date][0]
    date = '{}-{}-{}'.format(dateYear, dateMonth, dateDate)
    return date