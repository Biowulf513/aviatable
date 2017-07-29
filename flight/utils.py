# -*- coding: utf-8 -*-
from string import digits, ascii_uppercase



def code_generation(bad_text=None, text=''):
    import random
    if bad_text:
        text = ''
    while len(text) < 6:
        text += random.choice(list(digits + ascii_uppercase))

    return text
