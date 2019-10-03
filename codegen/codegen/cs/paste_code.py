def paste(code_item, code_to_paste):
    paste_range = find_paste_range(code_item.dest_file, code_item.start_key, code_item.end_key)
    start_line_index = paste_range[0] + code_item.start_offset
    end_line_index   = paste_range[1]
    replace_code(code_item.dest_file, start_line_index, end_line_index, code_to_paste)

def find_paste_range(dest_file, start_key, end_key):
    with open(dest_file) as destination_cs:
        start_line_index = 0
        end_line_index = 0
        for line_number, line in enumerate(destination_cs, 1):
            if start_line_index == 0:
                if start_key in line:
                    start_line_index = line_number-1
            else:
                if line.strip() == end_key:
                    end_line_index = line_number-1
                    break
    return (start_line_index, end_line_index)

def replace_code(dest_file, start_line_index, end_line_index, code_to_paste):
    try:
        cs_destination = open(dest_file, "r+", encoding='utf8')
        content = cs_destination.readlines()
        del content[start_line_index:end_line_index]        
        content[start_line_index:start_line_index] = code_to_paste
        cs_destination.seek(0)
        for line_number, line in enumerate(content, 1):
            cs_destination.write(line)
        cs_destination.truncate()
    finally:
        cs_destination.close()