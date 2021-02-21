import csv, os, re
import datetime

print("Start Time:", datetime.datetime.now())
print('Converting CSV to XML')

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'): continue
    xmlFileName = os.path.splitext(csvFilename)[0]
    print(xmlFileName)
    f = open(xmlFileName + '.xml' , 'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>')
    f.write('<Metadata>')
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    
    for row in readerObj:
        if readerObj.line_num == 1: continue
        #XML child elements
        fetchDate = re.match("[0-3]?[0-9]?[0-9]?[0-9]-[0-3]?[0-9]-[0-3]?[0-9]", row[1])
        print(fetchDate)
        appendTDate = format(fetchDate.group(0)) +'T'
        modifiedDate = re.sub(r'[0-3]?[0-9]?[0-9]?[0-9]-[0-3]?[0-9]-[0-3]?[0-9] ', appendTDate, row[1])
        f.write(' '+ '<Participant>')
        f.write(' '+ '<ExternalId>' + row[0] + '</ExternalId>')
        f.write(' '+ '<callTimeUTC>' + modifiedDate + '</callTimeUTC>')
        f.write(' '+ '<ConversationId>' + row[2] + '</ConversationId>')
        f.write(' '+ '<macAddress>' + row[3] + '</macAddress>')
        f.write(' '+ '<traderIDCTI>' + row[4] + '</traderIDCTI>')
        f.write(' '+ '<rectype>' + row[5] + '</rectype>')
        f.write(' '+ '<direction>' + row[6] + '</direction>')
        f.write(' '+ '<ownPhoneNumber>' + row[7] + '</ownPhoneNumber>')
        f.write(' '+ '<partnerPhoneNumber>' + row[8] + '</partnerPhoneNumber>')
        f.write(' '+ '<dialedName>' + row[9] + '</dialedName>')
        f.write(' '+ '<audio_source>' + row[10] + '</audio_source>')
        f.write(' '+ '<internal_external>' + row[11] + '</internal_external>')
        f.write(' '+ '</Participant>')
    #XML end root element
    f.write('</Metadata>')
    f.close()
    csvFileObj.close()

print('Done converting CSV to XML!! Please check current directory.')
print("End Time:", datetime.datetime.now())

for csvFilename in os.listdir('.'):
    if csvFilename.endswith('.csv'):
        os.remove(csvFilename)



