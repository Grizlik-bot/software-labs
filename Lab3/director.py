from query_builder import QueryBuilder

class Director:
    def __init__(self, builder: QueryBuilder):
        self.builder = builder

    def construct_query(self, columns: str, conditions: str, limit: int) -> str:
        return self.builder.select(columns).where(conditions).limit(limit).get_sql()
