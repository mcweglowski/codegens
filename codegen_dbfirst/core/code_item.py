class code_item(object):
    columns = []
    def __init__(self, table_name, entity_name):
        self.table_name  = table_name
        self.entity_name = entity_name