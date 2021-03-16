import xml.etree.ElementTree as ET

#with open(r'D:\SachinXML\Network_201201_020521_204527_001_520ST48602_51859930_XmlDepositReport.dat', 'rb') as data:
#    data = ET.fromstring(data)
f = open(r'D:\SachinXML\Network_201201_020521_204527_001_520ST48602_51859930_XmlDepositReport.dat', 'r')
fread = f.read()
#print (fread)
#export_data = "\'''", + str(fread) + "\'''"
#print (export_data)

data = ET.fromstring(fread.strip())

abcd = {}

def abc(root_tag):
    if root_tag.tag == "Counter":

        if root_tag.tag in abcd.keys():
            abcd["Counter"].append(root_tag.attrib)            
        else:
            abcd.update({"Counter" : [root_tag.attrib]})

    else:
        abcd.update({root_tag.tag : root_tag.attrib})

    for i in root_tag.getchildren():
        abc(i)
        #print (abc(i))
        
print (abc(data))
#print (abcd)
for j in abcd['Counter']:
    print (j['DenomID'])
    print(j)
#for key,value in abcd.items():
#    print (key,value)
list_of_machineK = []
list_of_machineV = []

#print (type(abcd['Machine']))

for machine_key,machine_value in abcd['Machine'].items():
    (list_of_machineK.append((abcd['Machine'][machine_key])))
    
print (list_of_machineK)
print (list_of_machineV)

