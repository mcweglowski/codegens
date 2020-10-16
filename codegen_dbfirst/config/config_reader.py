import json
from core import code_item
from core import destination_item
from config.config import config

def read_config():
    file_content = open('config.json').read()
    json_content = json.loads(file_content)
    tables = [code_item.code_item(**item) for item in json_content['source_tables']]
    connection_str = json_content['connection_string']
    destination_items = [destination_item.destination_item(**item) for item in json_content['destination']]
    return config(connection_str, tables, destination_items)