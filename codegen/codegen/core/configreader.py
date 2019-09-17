import json
from core.codeitem import code_item

def readcodeitems():
    content = open('config.json')
    contentstring = content.read()
    codeitems = [code_item(**item) for item in json.loads(contentstring)]
    return codeitems