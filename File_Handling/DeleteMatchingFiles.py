import csv, os, re
import datetime

csvFileObj = open('C:\\Users\\ShivanandVithal\\Documents\\IshProjects\\ASC\\ConversationIDs\\ImportedID.csv', encoding='utf-8')
readerObj = csv.reader(csvFileObj)
print(readerObj)

for row in readerObj:
    id = row[0]
    search_path = 'C:\\Users\\ShivanandVithal\\Documents\\IshProjects\\ASC\\ConversationIDs\\'
    for fname in os.listdir(search_path):
        if fname.endswith('.xlsx'):
            fo = open(search_path + fname)
            while line != '':
                search_str = 'Conversation_ID'
                index = line.find(search_str)
                if (index != -1):
                    print(fname)

                    # Read next line
                line = fo.readline()

            fo.close