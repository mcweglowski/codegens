from config import config_reader
from database import tables_reader

def run():
    config = config_reader.read_config()
    tables_reader.read(config.connection_string, config.tables)
    print('wait...')