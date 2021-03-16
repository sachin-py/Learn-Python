'''from xml.etree import ElementTree as ET

with open(r'Network_201201_020521_204527_001_520ST48602_51859930_XmlDepositReport.dat', 'r') as data:
    abcd = data.read()
parsed_data = ET.fromstring(abcd)
Tags = []
Text = []
Attribute = []
def abc(root_tag):
    if not list(root_tag.getchildren()) == []:
       # print ("Baap :", root_tag.tag)
        #print("Baap ke bacchhe : ", list(root_tag.getchildren()))
        #print("Baap ke items : ", root_tag.items())
        for i in root_tag.getchildren():
            if i.tag == "Operator":
                #print("Bacche :", i.tag, i.text)
                #Tags.append(i.tag)
                Text.append(i.text)
            else:
                #print ("Bacche :", i.tag, i.attrib)
                Tags.append(i.tag)
                Attribute.append(i.attrib)
            abc(i)
abc(parsed_data)
print ('Tags are: ',Tags)
print ('Text are: ',Text)
print ('Attributes are: ',Attribute[3][])'''

# print ('original data ',abcd)
# print ('parsed data ',parsed_data)

# print ('parsed data ',parsed_data)'''


from xml.etree import ElementTree as ET
import os

files = []
path = 'D:\SachinXML'
file = os.listdir(path)
#print (file)

for xml in file :
	if 'XmlDep' in xml:
		files.append(xml)

print ('XMLDeposit Files are : ',files)

def depositID(files):
	depID = files[0].split('_')
	print (depID)
	return depID[6]

depID_rep = depositID(files)

dep_name = []
for value in files:
	#print (value)
	dep_name.append(depositID(files))
print ("Deposit ID names : ",dep_name)


with open(r'Network_201201_020521_204527_001_520ST48602_51859930_XmlDepositReport.dat', 'r') as data:
    abcd = data.read()
parsed_data = ET.fromstring(abcd)
Tags = []
Text = []
Attribute = []
def abc(root_tag):
    if not list(root_tag.getchildren()) == []:
       # print ("Baap :", root_tag.tag)
        #print("Baap ke bacchhe : ", list(root_tag.getchildren()))
        #print("Baap ke items : ", root_tag.items())
        for i in root_tag.getchildren():
            if i.tag == "Operator":
                #print("Bacche :", i.tag, i.text)
                #Tags.append(i.tag)
                Text.append(i.text)
            else:
                #print ("Bacche :", i.tag, i.attrib)
                Tags.append(i.tag)
                Attribute.append(i.attrib)
            abc(i)
abc(parsed_data)
print ('Tags are: ',Tags)
print ('Text are: ',Text)
print ('Attributes are: ',Attribute[3]["HeaderCardID"])
HeaderCard = Attribute[3]["HeaderCardID"]

if HeaderCard == depID_rep:
	print ("Pass,Deposit ID in Report Name and in content is same")
else:
	print ("Not Same")



# print ('original data ',abcd)
# print ('parsed data ',parsed_data)'''