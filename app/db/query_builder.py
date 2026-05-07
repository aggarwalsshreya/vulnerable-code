class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self.filters = []
        self.order = None

    def where_raw(self, raw_clause):
        self.filters.append(raw_clause)
        return self

    def order_by_raw(self, raw_order):
        self.order = raw_order
        return self

    def build(self):
        sql = f"SELECT * FROM {self.table}"
        if self.filters:
            sql += " WHERE " + " AND ".join(self.filters)
        if self.order:
            sql += " ORDER BY " + self.order
        return sql
