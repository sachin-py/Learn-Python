import xml.etree.ElementTree as ET
import os

Data = dict()
files = []
HeaderCardIDofReport = []
ActualDepositID = []
depIDList = []
depID_zero = []
basePath = 'C:\\Python Learning\\Reports\\'
file = os.listdir(basePath)
print(file)
for xml in file:
    if 'Network' in xml:
        files.append(xml)
# print ('XMLDeposit Files are : ',files)

for dep_ID in files:
    depID = dep_ID.split('_')
    # print (depID[6])
    depIDList.append(depID[6])


# print (depIDList)
# depSet = set(depIDList)

def abc(root_tag):
    if root_tag.tag == "Counter":
        if root_tag.tag in Data.keys():
            Data["Counter"].append(root_tag.attrib)
        else:
            Data.update({"Counter": [root_tag.attrib]})
    else:
        Data.update({root_tag.tag: root_tag.attrib})

    tags = []
    attrib = []
    texts = []

    for i in root.iter():
        # print (i.tag,i.attrib,i.text)
        tags.append(i.tag)
        attrib.append(i.attrib)
        texts.append(i.text)
        if i == 0:
            abc(i)

    HeaderCardIDofReport.append(attrib[5]['HeaderCardID'])
    # print (attrib[4]['HeaderCardID'])
    ActualDepositID.append(attrib[5]['DepositID'])


for file_num in range(0, len(files)):
    #  print (file_num)
    path = basePath + '\\' + files[file_num]
    #  print ('path is ',path)
    tree = ET.parse(path)
    #  print ('Tree is :',tree)
    root = tree.getroot()

    abc(root)

print('Header Card ID of All Report : ', HeaderCardIDofReport)
print('Actual Deposit ID of Reports : ', ActualDepositID)

for val in depIDList:
    val = '00'+str(val)
    depID_zero.append(val)
print("New Deposit ID from Filename : ", depID_zero)

if HeaderCardIDofReport == depIDList:
    print('All Files are equal Header Card ID and Filename ID')
else:
    print('All Files are not equal')

if depID_zero == ActualDepositID:
    print('All Files are equal Deposit ID and Filename ID')
else:
    print('All Files are not equal')
