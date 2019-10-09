def add_code(destination_item, entity_name, generated_code):
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


    print('end')


#def add_code(destination_item, generated_code):
#    mydoc = minidom.parse(destination_item.destination_proj)
#    nodes_list = mydoc.getElementsByTagName('ItemGroup')
#    compile_node = findCompileNode(nodes_list)
#
#    new_node = mydoc.createElement("Test")
#    compile_node.appendChild(new_node)
#
#    with open(destination_item.destination_proj, 'w', encoding='utf8') as file:
#        file.write(mydoc.toxml())



#    print('end')
#
#def findCompileNode(nodes_list):
#    for node in nodes_list:
#        for childNode in node.childNodes:
#            if childNode.nodeName == "Compile":
#                return node
#    return None


#import xml.etree.ElementTree as ET
#
#
#def add_code(destination_item, generated_code):
#    tree = ET.parse(destination_item.destination_proj)
#    root = tree.getroot()
#        
#    for child in root:
#        print(child.tag, child.attrib)
#    print('End')