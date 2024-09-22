from query_builder import QueryBuilder

class PostgreSQLBuilder(QueryBuilder):
    def __init__(self):
        self.query = []

    def select(self, columns: str) -> 'PostgreSQLBuilder':
        self.query.append(f"SELECT {columns} FROM")
        return self

    def where(self, conditions: str) -> 'PostgreSQLBuilder':
        self.query.append(f"WHERE {conditions}")
        return self

    def limit(self, limit: int) -> 'PostgreSQLBuilder':
        self.query.append(f"LIMIT {limit}")
        return self

    def get_sql(self) -> str:
        return " ".join(self.query) + ";"
