import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-p',
                    dest='pedantic',
                    action='store_true',
                    help='Words need to be exactly the same, if off, checks if one word contains the other')

pedantic = parser.parse_args().pedantic

if len(sys.argv) < 2:
    print('Missing filename argument')
    exit(1)

fileName = sys.argv[1]

txt = Path(fileName).read_text()
txt.replace('\n', '')

sentences = txt.split('.')

previousWord = ''
counter = 0
for sentence in sentences:
    words = sentence.split(' ')
    counter += 1
    for word in words:
        if '-' in word:
            subwords = word.split('-')
            for w in subwords:
                if pedantic:
                    if word == previousWord:
                        print(word)
                        print(str(counter) + ': ' + sentence)
                else:
                    if word in previousWord or previousWord in word:
                        print(word)
                        print(str(counter) + ': ' + sentence)

        if pedantic:
            if word == previousWord:
                print(word)
                print(str(counter) + ': ' + sentence)
        else:
            if word in previousWord or previousWord in word:
                print(word)
                print(str(counter) + ': ' + sentence)
        previousWord = word

