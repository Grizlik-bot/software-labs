from query_builder import QueryBuilder

class MySQLBuilder(QueryBuilder):
    def __init__(self):
        self.query = []

    def select(self, columns: str) -> 'MySQLBuilder':
        self.query.append(f"SELECT {columns} FROM")
        return self

    def where(self, conditions: str) -> 'MySQLBuilder':
        self.query.append(f"WHERE {conditions}")
        return self

    def limit(self, limit: int) -> 'MySQLBuilder':
        self.query.append(f"LIMIT {limit}")
        return self

    def get_sql(self) -> str:
        return " ".join(self.query) + ";"
