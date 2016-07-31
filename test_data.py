#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from random import randint

def getData():

    # получить количество ФИО
    with open(sys.path[0] + '/names.txt') as f:
        users_data = f.readlines()

    max_value = len(users_data)
    invalid_random = randint(max_value + 1, max_value + 100000)

    test_data = [
        {
            'name': 'id',
            'value': randint(1, max_value),
            'result': 'json',
        },
        {
            'name': 'id',
            'value': 0,
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': 0.5,
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': -1,
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': 'sometext',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': 'какойтотекст',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': '!"№;%:?*,_+=-',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': '',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': ' ',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': '1a',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': '1.',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': '1 ',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': ' 1',
            'result': 'Invalid "id" value',
        },
        {
            'name': 'id',
            'value': invalid_random,
            'result': 'User with "id" = %i not exist' % invalid_random,
        },
        {
            'name': 'not_id',
            'value': randint(1, max_value),
            'result': '400',
        },
        {
            'name': '',
            'value': randint(1, max_value),
            'result': '400',
        },
        {
            'name': ' ',
            'value': randint(1, max_value),
            'result': '400',
        },
        {
            'name': 0,
            'value': randint(1, max_value),
            'result': '400',
        },
        {
            'name': '',
            'value': invalid_random,
            'result': '400',
        },
    ]

    return test_data