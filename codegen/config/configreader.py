import json
from codegen.core.codeitem import code_item
from codegen.config import config

def readcodeitems():
    content = open('codegen.json')
    contentstring = content.read()
    codeitems = [code_item(**item) for item in json.loads(contentstring)]
    return codeitems

def read():
    file_content = open('codegn.json').read()
    json_content        = json.loads(file_content)
    source_path         = json_content['sourcepath']
    source_tabs         = json_content['source_tabs']
    start_search_row    = json_content['start_search_row']
    column_range_start  = json_content['column_range_start']
    column_range_stop   = json_content['column_range_stop']
    code_items       = [code_item(**item) for item in json_content['code_items'] if item['is_active'] == True]
    config_data      = config.config(source_path, source_tabs, code_items, start_search_row, column_range_start, column_range_stop)
    return config_data