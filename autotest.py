#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
from flask import json
import web_service
from test_data import getData

class webAppAutotest():
    url = 'http://127.0.0.1:5000'
    test_logs = sys.path[0] + '/log.txt'
    error_counter = 0

    def __init__(self):
        self.logs = open(self.test_logs, 'w')

    def sendPostRequest(self, name, value):
        r = requests.post(self.url, data={name:value})
        return r.text

    def sendGetRequest(self):
        r = requests.get(self.url)
        return r.text

    def checkAllTestData(self):
        all_test_data = getData()
        for data in all_test_data:
            result = self.sendPostRequest(data['name'], data['value'])
            if data['result'] == 'json':
                try:
                    self.checkJson(json.loads(result), data['value'])
                except:
                    self.printError("With request body like %s=%s test is failed."
                                    "\n Expecter result: some %s"
                                    "\n Actual result: %s"
                                    % (data['name'], data['value'], data['result'], result[:300]))
            else:
                if data['result'] not in result:
                    self.printError("With request body like %s=%s test is failed."
                                    "\n Expecter result: %s"
                                    "\n Actual result: %s"
                                    % (data['name'], data['value'], data['result'], result[:300]))

        result = self.sendGetRequest()
        if result != 'Welcome to test web-service. Please use POST request to get json with full user name':
            self.printError("GET request must return text '%s'\nActual request is: '%s'"
                            % (web_service.GET_text, result[:300]))

        if self.error_counter == 0:
            print "All tests is OK"
        self.logs.close()

    def checkJson(self, data, id):
        data_keys = data.keys()
        keys = ['last_name', 'first_name', 'patronymic']
        for key in keys:
            if key not in data_keys:
                self.printError('Not found "%s" key in response, founded by id=%s' % (key, str(id)))
            if len(data[key]) == 0 or len(data[key].replace(' ', '')) == 0:
                self.printError('Empty value "%s" in response, founded by id=%s' % (key, str(id)))

    def printError(self, text):
        print text
        self.logs.write(text + "\n-----\n")
        self.error_counter += 1

if __name__ == "__main__":
    webAppAutotest().checkAllTestData()