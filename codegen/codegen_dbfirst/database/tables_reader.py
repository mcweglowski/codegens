import pyodbc
from database import queries
from core.column import column

def read(connection_string, code_items):
    tables_configuration = get_tables_configuration(connection_string, code_items)
    for item in code_items:
        item.columns = [column(c.column_name, c.data_type, c.max_length, c.precision, c.scale, c.is_nullable, c.primary_key, c.index_name) 
                        for c in tables_configuration if c.table_name == item.table_name]

def get_tables_configuration(connection_string, code_items):
    tables = ["\'{}\'".format(code_item.table_name) for code_item in code_items]
    query = queries.tables_definition.format(tables = ",".join(tables))

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    rows = cursor.execute(query).fetchall()
    return rows
