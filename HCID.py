import xml.etree.ElementTree as ET
import os
import pandas as pd

files = []
basepath = 'C:\\Python Learning\\Reports'
file = os.listdir(basepath)
#print (file)
for xml in file :
    if 'rpt1030' in xml:
        files.append(xml)
#print ('XMLDeposit Files are : ',files)

depIDlist  = []
for dep_ID in (files):
    depID = dep_ID.split('_')
    #print (depID[6])
    depIDlist.append(depID[7])
print ('Filename ID : ',depIDlist)

#----------------Writing to a list--------------------#
df = pd.DataFrame(depIDlist)
df.to_excel('Deposit ID.xlsx',sheet_name = 'HC ID',index = False)
#print (df)
#--------------Reading through excel file and converting to list-----------------------#
newls = pd.read_excel('C:\\Python Learning\\Deposit ID2.xlsx')
ls = newls[0].tolist()
#print (ls)
str_ls = []
for val in ls:
	str_ls.append(str(val))
print ('List of Excel : ',str_ls)
DepListOfExcel = set(str_ls)
DepIDfromReportName = set(depIDlist)
set_diff = DepListOfExcel-DepIDfromReportName
#set_diff = DepListOfExcel.difference_update(DepIDfromReportName)
#print (set_diff)
if set_diff is None:
	print ('Reports are available')
else:
	print ('Reports are not available for : ',set_diff)
