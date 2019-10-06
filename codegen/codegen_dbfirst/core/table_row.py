class table_row(object):
    def __init__(self, column_name, data_type, max_length, precision, scale, is_nullable, primary_key):
        self.column_name = column_name
        self.data_type   = data_type
        self.max_length  = max_length 
        self.precision   = precision 
        self.scale       = scale
        self.is_nullable = is_nullable 
        self.primary_key = primary_key