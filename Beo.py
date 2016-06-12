#!/usr/bin/env python

import json
import sys
# import pprint

CAESURA = '    '
trans = []
orig = []

# with open('Beowulf.1245.to.1260.json', 'r', encoding='utf-8') as f:
with open('Beowulf.1245.to.1260.json', 'r') as f:
    data = json.load(f)


def origAppend(elem, punc=False):
    '''Append element to original line'''
    if punc:
        orig[-1] += elem
    else:
        orig.append(elem)


def transAppend(punc):
    '''Append punctuation to last translation element'''
    trans[-1] += punc


def printLine():
    '''Print out the line - original and translation'''
    global trans, orig
    sys.stdout.write(' '.join(orig) + "\t" + ' '.join(trans) + "\n")
    trans = []
    orig = []

for d in data:
    if 'section-heading' in d:
        origAppend("Section {0}".format(d['section-heading']))
    if 'line' in d:
        origAppend("Line {0} ".format(d['line']))
    if 'content' in d:
        for contents in d['content']:
            if 'word' in contents:
                origAppend(contents['word'])
                trans.append(contents['trans'][0])
            if 'punc' in contents:
                origAppend(contents['punc'], True)
                transAppend(contents['punc'])
            if 'caesura' in contents:
                origAppend(CAESURA)
    origAppend("\t")
    printLine()
    # sys.stderr.write("\n")
