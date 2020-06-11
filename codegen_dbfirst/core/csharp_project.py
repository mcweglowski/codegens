def add_code(destination_item, entity_name, generated_code):
    add_in_csproj(destination_item, entity_name)
    add_file(destination_item, entity_name, generated_code)


def add_file(destination_item, entity_name, generated_code):
    file_name = destination_item.file_name.format(entity_name)
    file_path = destination_item.destination_file_path + file_name

    dest_file = open(file_path, "w+", encoding='utf8')
    for line_number, line in enumerate(generated_code, 1):
        dest_file.write(line)
    dest_file.truncate()
    dest_file.close()

def add_in_csproj(destination_item, entity_name):
    file_content = []
    with open(destination_item.destination_proj, 'r') as dest_file:
        file_content = dest_file.readlines()        
    index = len(file_content) - 1

    pattern = destination_item.csproj_search_pattern    
    while 0 <= index:
        if pattern in file_content[index]:
            break
        index -= 1
    
    if -1 == index:
        print('Compile section not found')

    new_line = ''
    if destination_item.inner_folder == '':
        new_line = "    <Compile Include=\"{file_name}\" />\n".format(file_name = destination_item.file_name.format(entity_name))
    else:
        new_line = "    <Compile Include=\"{inner_folder}\\{file_name}\" />\n".format(inner_folder = destination_item.inner_folder, file_name = destination_item.file_name.format(entity_name))

    file_content.insert(index+1, new_line)

    with open(destination_item.destination_proj, 'w') as dest_file:
        for line_number, line in enumerate(file_content, 1):
            dest_file.write(line)
        dest_file.truncate()
        dest_file.close()