import re


class Query:

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
        where_clause = m.group(1) + "=" + "'" + m.group(2) + "'"
        return where_clause

    def __init__(self, query):
        self.table =  self.get_table(query)
        self.fields = self.get_query_field(query)
        self.whereClause = self.get_query_condition(query)

    def build_query_str(self):
        query_str = "select %s from %s where %s " % (self.fields, self.table, self.whereClause)
        return query_str



