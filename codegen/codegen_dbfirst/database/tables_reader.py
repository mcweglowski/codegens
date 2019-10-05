import pyodbc
from database import queries

def read(connection_string, code_items):
    connection = pyodbc.connect(connection_string)

    cursor = connection.cursor()
    tables = ["\'{}\'".format(code_item.table_name) for code_item in code_items]
    query = queries.tables_definition.format(tables = ",".join(tables))
    print(query)

