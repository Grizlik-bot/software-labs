from abc import ABC, abstractmethod

class QueryBuilder(ABC):
    @abstractmethod
    def select(self, columns: str) -> 'QueryBuilder':
        pass

    @abstractmethod
    def where(self, conditions: str) -> 'QueryBuilder':
        pass

    @abstractmethod
    def limit(self, limit: int) -> 'QueryBuilder':
        pass

    @abstractmethod
    def get_sql(self) -> str:
        pass
