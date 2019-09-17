class code_item(object):
    def __init__(self, dest_file, start_key, start_offset, end_key, line_pattern):
        self.dest_file    = dest_file
        self.start_key    = start_key
        self.start_offset = start_offset
        self.end_key      = end_key
        self.line_pattern = line_pattern