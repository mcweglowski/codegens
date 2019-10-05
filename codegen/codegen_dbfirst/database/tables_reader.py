import pyodbc
from database import queries

def read(connection_string, code_items):
    tables_configuration = get_tables_configuration(connection_string, code_items)
    for item in code_items:
        item.columns = [column_def for column_def in tables_configuration if column_def.table_name == item.table_name]

def get_tables_configuration(connection_string, code_items):
    tables = ["\'{}\'".format(code_item.table_name) for code_item in code_items]
    query = queries.tables_definition.format(tables = ",".join(tables))

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    rows = cursor.execute(query).fetchall()
    return rows
