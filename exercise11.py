# coding=utf-8
from random import shuffle
from sys import exit

fname = input('Please insert file name: ')
try:
    fhandle = open(fname, 'r')
except FileNotFoundError:
    print('File not found! exiting..')
    exit(1)

contents = fhandle.read()
words = contents.split()
words_len = len(words)

triads = []

for i in range(words_len - 2):
    triads.append(words[i:i+3])

print('\nText stored as overlapping triads:\n', triads)

shuffle(triads)
random_text = ''

for triad in triads:
    random_text += ' '.join(triad) + ' '
random_text.strip()

print('\nNew random text created:\n', random_text)
