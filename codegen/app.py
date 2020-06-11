from config import configreader
from cs import paste_code
from core.codeitem import code_item
from excel import excel_reader

def run():
    config_data = configreader.read()
    excel_data  = excel_reader.read(config_data)
    for item in config_data.code_items:
        code = item.generate_code(excel_data)
        paste_code.paste(item, code)