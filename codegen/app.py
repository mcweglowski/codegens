from codegen.config import configreader
from codegen.cs import paste_code
from codegen.core.codeitem import code_item
from codegen.excel import excel_reader

from colorama import init
from colorama import Fore


init()

def run():
    print(Fore.GREEN + 'Codegen begin')
    print(Fore.YELLOW + 'Loading config file')
    config_data = configreader.read()
    print(Fore.GREEN + 'Loading config file finished')

    print(Fore.YELLOW + 'Reading ' + config_data.source_path + ' file')
    excel_data  = excel_reader.read(config_data)
    print(Fore.GREEN + 'Reading ' + config_data.source_path +' file finished')

    if excel_data is None:
        print(Fore.RED + 'File is not accessible: ' + config_data.source_path)
        print(Fore.GREEN + 'Codegen finished with no effects.')
        return
    
    for item in config_data.code_items:
        print(Fore.YELLOW + 'Generate code for ' + item.dest_file)
        code = item.generate_code(excel_data)
        print(Fore.GREEN + 'Generate code for ' + item.dest_file + ' finished')
        print(Fore.YELLOW + 'Pasting code into ' + item.dest_file)
        paste_code.paste(item, code)
        print(Fore.GREEN + 'Pasting code into ' + item.dest_file + ' finished')
    print(Fore.GREEN + 'Codegen finish')