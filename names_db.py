#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

class names(object):
    def __init__(self):
        self.connect()
        self.clearTable()
        self.createTestData()
        self.close()

    def connect(self):
        self.db = sqlite3.connect('names.db')
        self.cur = self.db.cursor()

    def close(self):
        self.db.close()

    def createTable(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS names (id INTEGER PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), patronymic VARCHAR(255))')
        self.db.commit()

    def createTestData(self):
        with open(sys.path[0] + '/names.txt') as f:
            users_data = f.readlines()
        for user_data in users_data:
            data = user_data.split('|')

            self.id = data[0]
            self.first_name = data[1]
            self.last_name = data[2]
            self.patronymic = data[3].replace("\n", '')
            params = (self.id, self.first_name, self.last_name, self.patronymic)

            self.cur.execute(
                'INSERT INTO names (id, first_name, last_name, patronymic) VALUES (?,?,?,?)', params)
            self.db.commit()

    def clearTable(self):
        self.cur.execute('DROP TABLE IF EXISTS names')
        self.createTable()

    def getFullNameById(self, id):
        self.connect()
        self.cur.execute('SELECT first_name, last_name, patronymic FROM names WHERE id = %i' % id)
        items = self.cur.fetchall()
        self.close()
        return items