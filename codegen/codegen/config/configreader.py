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
    json_content = json.loads(file_content)
    source_path  = json_content['sourcepath']
    source_tab   = json_content['sourcetab']
    dest_folder  = json_content['destfolder']
    code_items   = [code_item(**item) for item in json_content['code_items']]
    config_data  = config.config(source_path, source_tab, dest_folder, code_items)
    return config_data