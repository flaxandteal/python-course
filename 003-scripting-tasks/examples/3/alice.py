#!/usr/bin/env python3

import nltk
import sys
import collections

lines = sys.stdin.read()

# Natural Language researcher magic...
tokens = nltk.word_tokenize(lines)
body_of_text = nltk.Text(tokens)
words_labelled_by_type = nltk.pos_tag(body_of_text)

# Back to more standard Python
type_of_each_word = [t for word, t in words_labelled_by_type]
types_by_frequency = collections.Counter(type_of_each_word)

print("There are %d verbs in this text" % types_by_frequency['VB'])
