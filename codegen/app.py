from codegen.config import configreader
from codegen.cs import paste_code
from codegen.core.codeitem import code_item
from codegen.excel import excel_reader

def run():
    print('Codegen begin')
    config_data = configreader.read()
    excel_data  = excel_reader.read(config_data)
    
    if excel_data is None:
        print('File is not accessible: ' + config_data.source_path)
        return
    
    for item in config_data.code_items:
        code = item.generate_code(excel_data)
        paste_code.paste(item, code)
    print('Codegen Finish')