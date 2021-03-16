from xml.etree import ElementTree

with open(r'D:\SachinXML\BPS_201201_rpt1035_020521_204528_001_520ST48602_0051859930_XmlTicketReport.dat', 'rt') as f:
    tree = ElementTree.parse(f)
all_data = []
for node in tree.iter():
   #print (node.tag)
   #print (node.attrib)
   #print (node.tag,node.attrib)
    all_data.append(node.attrib)
    

#print (all_data[5])
#print (all_data[6:])
myList = all_data[6:]
print (myList)
#-----------------------------

import pandas as pd

a = pd.DataFrame(myList)
print (a)
a.to_excel('PDTicketexcl.xls',index = False)
#------------------------


'''
#print ("my list is : ", myList)
input_str = myList[0].keys()
#print (type(input_str))
#print (input_str)

keyname = []
keyvalue = []

for ky in input_str:
    keyname.append(ky)
    #print (keyname)
#print (keyname)

input_value = myList[0].values()
#print (input_value)
for vl in input_value:
    keyvalue.append(vl)
    #print (keyvalue)
#print (keyvalue)

#print (all_data)
#print (all_data[6:])

all_key = []
all_value = []
for i in all_data[6:]:
	#print (i)
	for k,v in i.items():
		all_key.append(k)
		all_value.append(v)

#print ('all keys are : ',all_key[:7])
#print ('all values are : ',all_value)

elements = all_key[:6]
#print (elements)
#print (all_value)

import xlsxwriter 
  
workbook = xlsxwriter.Workbook('TicketReport.xlsx') 
worksheet = workbook.add_worksheet('1st Report') 
row = 5       #initial Value is 0 
column = 0    #initial Value is 0 
for item in elements:
	worksheet.write(row, column, item) 
	column = column+1

row2 = 6       #initial Value is 1
column2 = 0    #initial Value is 0
for item2 in all_value:
	print(row2,column2,item2)
	#worksheet.write(row2 , column2, item2)
	if (column2%6 == 0) & (column2!=0):
		row2 = row2+1
		column2 = 0
	worksheet.write(row2 , column2, item2)
	column2 = column2+1

#print (column2)

workbook.close()

'''