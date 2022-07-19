#!/usr/bin/python

import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='Output file. If file already exists, the new words will be added to it.')
    parser.add_argument('-i', '--input', help='Input file. ')
    FIXME

def file_reader(filename):
    text_lines = []
    with open(filename, 'r') as textfile:
        text_lines = [x.strip() for x in textfile.readlines()]
    return text_lines

def file_writer(filename, data):
    with open(filename, 'w') as outfile:
        for i in data:
            outfile.write(f"{i}\n")

def wordify(text):
    """ Turns chunks of text into single words. """
    dirty_words = []
    for line in text:
        dirty_words = dirty_words + line.split(' ')
    clean_words = []
    for word in dirty_words:
        if word == '...':
            word = None
        elif len(word) < 2:
            word = None
        elif word == '-':
            word = None
        elif word[-1] == '.' or word[-1] == ',':
            word = word[0:-1]
        elif word[-1] == '-' or word[-1] == ':':
            word = word[0:-1]
        else:
            pass
        if word and word not in clean_words:
            clean_words.append(word.lower())
    return clean_words




data = file_reader('vlastovka.txt')
words = wordify(data)
print(words)
file_writer('redl.txt', words)

