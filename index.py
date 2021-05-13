import json
import random
import re

text = ''
massifTem = []


def setText(text, input):
    text = ' ' + input
    return text


with open("data/dataPtactic.json", encoding="utf8") as json_file:
    data = json.load(json_file)

text = text + '\n ' + data['pm1'][0][1]
text = text + '\n ' + data['pm1'][0][0]
text = text + '\n ' + data['pm4'][1][0]
text = text + '\n ' + data['pm4'][0][0]

for i in range (20):
    intPm = str(random.randint(1, 5))
    intPmTema = random.randint(0, len(data['pm' + intPm])-1)
    if intPmTema == 0 and intPm == 1:
        intPmTema = 2
    intPmTemaWord = random.randint(0, len(data['pm' + intPm][intPmTema])-1)
    if data['pm' + intPm][intPmTema][intPmTemaWord] in text:
        pass
    else:
        text = text + '\n ' + data['pm' + intPm][intPmTema][intPmTemaWord]

print(text)
