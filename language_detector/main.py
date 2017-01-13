# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    lang=''
    select=0
    newlist=text.split(' ')
    for x in languages:
        #print([n for n in x['common_words'] if n in newlist])
        a=len([n for n in x['common_words'] if n in newlist])
        if a>select:
            select=a
            lang=x['name']
        '''
#        print(x['common_words'])
        a=0
        for y in newlist:   
            a+=x['common_words'].count(y)
        if a>select:
            select=a
            lang=x['name']
        '''

    return lang
