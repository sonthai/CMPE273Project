import re
import requests

class Query:
    rest_api_url = 'https://itvdw1grqh.execute-api.us-west-2.amazonaws.com/v1/class-syllabus'

    def get_table(self, sparql):
        regex = 'table:(\w+)'
        m = re.search(regex, str(sparql))
        return m.group(1)

    def get_query_field(self, sparql):
        regex = 'key:fields "(.*)"'
        m = re.search(regex, str(sparql))
        fields = m.group(1).split(",")
        fieldList = []
        for field in fields:
            fieldList.append("_".join(field.split(" ")))
        return ",".join(fieldList)

    def get_query_condition(self, sparql):
        regex = 'key:(\w+) keyword:(.*).'
        m = re.search(regex, str(sparql))
        return m.group(2)

    def get_answer(self, sparql):
        regex = 'key:answer "(.*)"'
        m = re.search(regex, str(sparql))
        answer =  m.group(1)
        return answer

    def __init__(self, query):
        self.table =  self.get_table(query)
        self.fields = self.get_query_field(query)
        self.course = self.get_query_condition(query)
        self.answer = self.get_answer(query)

    def query_for_answer(self):
        #query_str = "select %s from %s where %s = '%s' " % (self.fields, self.table, self.key, self.keyword)
        # temporary. Replace it wiht real answer
        #data = "Finish 272"
        #reply = self.answer % (self.keyword, data)
        #return query_str, reply
        jsonStr = {
            'table': self.table,
            'field': self.fields,
            'course': self.course,
            "answer": self.answer
        }
        response =  requests.post(self.rest_api_url, json=jsonStr)

        return str(response.json()['response'])






