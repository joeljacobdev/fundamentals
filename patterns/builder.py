from typing import List


# build complex objects having chaining of methods
# for example to form django query - queryset is chained with methods to modify the queryset


class QueryBuilder:

    def __init__(self):
        self._table = NotImplemented
        self._select_fields = []
        self._filters = {}

    def set_table(self, table):
        self._table = table
        return self

    def values(self, fields: List[str]):
        self._select_fields.extend(fields)
        return self

    def filter(self, filter_dict: dict):
        for field, value in filter_dict.items():
            tokens = field.split('__')
            field_identifier = tokens[0]
            if len(tokens) == 1:
                op = '='
            else:
                op = tokens[-1]
            if isinstance(value, list):
                value = tuple(value)
            self._filters[field_identifier] = (op, value)
        return self

    def prepare_sql(self):
        select_fields = ','.join(self._select_fields) if self._select_fields else '*'
        where_clause = ''
        if self._filters:
            where_clause = 'where'
            for field, (op, value) in self._filters.items():
                if where_clause != 'where':
                    where_clause = f'{where_clause} and'
                where_clause = f"{where_clause} {field} {op} {value}"
        sql = f"select {select_fields} from {self._table} {where_clause};"
        return sql


sql = QueryBuilder().filter({'community_user__in': [1, 4, 5], 'current_course': 3}).prepare_sql()
print(sql)
