import os
import re
import fileinput

pattern = re.compile("[0-3]?[0-9]?[0-9]?[0-9]-[0-3]?[0-9]-[0-3]?[0-9]")
dir_path = 'C:\\Users\\ShivanandVithal\\Downloads'
output_file = dir_path+"\\tmp.txt"

#check if temp file exists
if os.path.exists(output_file):
  os.remove(output_file)

for filename in os.listdir(dir_path):
    if not filename.endswith('.xml'): pass
    print("here")
    tempFile = open(output_file, 'w+')
    xml_filename = os.path.join(dir_path, filename)
    print(xml_filename)

    #get modified timestamp
    def getDateString():
        for line in fileinput.input(xml_filename):
            for match in re.finditer(pattern, line):
                dateString = match[0]
                dateString = dateString + 'T'
                fileinput.close()
                return dateString

    str_to_append = getDateString()
    for line in fileinput.input(xml_filename):
        line = re.sub(r'[0-3]?[0-9]?[0-9]?[0-9]-[0-3]?[0-9]-[0-3]?[0-9] ', str_to_append, line)
        tempFile.write(line)

    tempFile.close()

    copy_to_file = open(xml_filename, "w")
    with open(output_file, "r") as f:
        copy_to_file.write(f.read())

    os.remove(output_file)
