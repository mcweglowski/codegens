import json
from core.codeitem import code_item
from config import config

def readcodeitems():
    content = open('config.json')
    contentstring = content.read()
    codeitems = [code_item(**item) for item in json.loads(contentstring)]
    return codeitems

def read():
    file_content = open('config.json').read()
    json_content        = json.loads(file_content)
    source_path         = json_content['sourcepath']
    source_tab          = json_content['sourcetab']
    dest_folder         = json_content['destfolder']
    start_search_row    = json_content['start_search_row']
    column_range_start  = json_content['column_range_start']
    column_range_stop    = json_content['column_range_stop']
    code_items       = [code_item(**item) for item in json_content['code_items']]
    config_data      = config.config(source_path, source_tab, dest_folder, code_items, start_search_row, column_range_start, column_range_stop)
    return config_data