from mysql_builder import MySQLBuilder
from postgresql_builder import PostgreSQLBuilder
from director import Director

def main():
    mysql_builder = MySQLBuilder()
    director = Director(mysql_builder)
    mysql_query = director.construct_query("name, age", "age > 21", 10)
    print(f"MySQL Query: {mysql_query}")

    postgresql_builder = PostgreSQLBuilder()
    director = Director(postgresql_builder)
    postgresql_query = director.construct_query("name, age", "age > 21", 10)
    print(f"PostgreSQL Query: {postgresql_query}")

if __name__ == "__main__":
    main()
