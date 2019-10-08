from core import sqltocsharp

class destination_item(object):
    def __init__(self, destination_proj, destination_file_path, line_pattern, file_pattern):
        self.destination_proj      = destination_proj,
        self.destination_file_path = destination_file_path
        self.line_pattern          = line_pattern
        self.file_pattern          = "".join(file_pattern)

    def get_code(self, table):
        print("Table code: {}".format(table.table_name))
        columns_text = "".join([self.get_row(column) for column in table.columns])
        primary_key = self.get_primary_key(table.columns)
        file_content = self.get_file_content(table, columns_text, primary_key)
        return file_content

    def get_file_content(self, table, columns_text, primary_key):
        return self.file_pattern.format(entity_name  = table.entity_name, 
                                        table_name   = table.table_name, 
                                        columns_text = columns_text,
                                        primary_key  = primary_key)

    def get_row(self, column):
        return self.line_pattern.format(csharp_type = sqltocsharp.get_type(column.data_type, column.is_nullable),
                                        field_name = column.name,
                                        configuration = sqltocsharp.get_configuration(column.data_type, column.is_nullable, column.max_length, column.primary_key))

    def get_primary_key(self, columns):
        return "".join([column.name for column in columns if column.primary_key == True])