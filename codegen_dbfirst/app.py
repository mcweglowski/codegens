from config import config_reader
from database import tables_reader
from core import csharp_project

def run():
    config = config_reader.read_config()
    tables_reader.read(config.connection_string, config.tables)
    
    for destination in config.destination_items:
        for table in config.tables:
            code = destination.get_code(table)
            csharp_project.add_code(destination, table.entity_name, code)