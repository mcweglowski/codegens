class config(object):
    def __init__(self, connection_string, source_tables, destination_items):
        self.connection_string = connection_string
        self.tables = source_tables
        self.destination_items = destination_items