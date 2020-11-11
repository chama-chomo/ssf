#!/usr/bin/env python3
#-*-coding:utf-8-*-

from __future__ import print_function

from pick import Picker

def go_back(picker):
    return (None, -1)

def filtered(picker):
    return (1, 1)

title = 'Please choose your favorite programming language: '
options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']

picker = Picker(options, title)
picker.register_custom_handler(ord('/'), filtered)
option, index = picker.start()
print('option {} - index {}'.format(option, index))

option = input('\nChoose a filter: ')
options = [i for i in options if option in i]

picker = Picker(options, title)
picker.register_custom_handler(ord('/'), filtered)
option, index = picker.start()
