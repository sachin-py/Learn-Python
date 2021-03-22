import xml.etree.ElementTree as ET
import os
files = []
basepath = 'C:\\Python Learning\\Reports\\'
file = os.listdir(basepath)
#print (file)
for xml in file :
    if 'Network' in xml:
        files.append(xml)
#print ('XMLDeposit Files are : ',files)

depIDlist  = []
for dep_ID in (files):
    depID = dep_ID.split('_')
    #print (depID[6])
    depIDlist.append(depID[6])
#print (depIDlist)
depset = set(depIDlist)
#print ("set ",depset)

def abc(root_tag):
        if root_tag.tag == "Counter":
            if root_tag.tag in abcd.keys():
                abcd["Counter"].append(root_tag.attrib)            
            else:
                abcd.update({"Counter" : [root_tag.attrib]})
        else:
            abcd.update({root_tag.tag : root_tag.attrib})
        tags = []
        attrib = []
        texts = []
        
        for i in root.iter():
   #         print (i.tag,i.attrib,i.text)  
            tags.append(i.tag) 
            attrib.append(i.attrib) 
            texts.append(i.text)
                
            if (i)== 0:

                abc(i)
    #    print ('Tags are : ',tags)
     #   print ('Attrib are : ', attrib)
      #  print ('Texts are : ', texts)

        HeaderCardIDsofReport.append(attrib[5]['HeaderCardID'])
        ActualDepositID.append(attrib[5]['DepositID'])
        
        #print (attrib[5]['DepositID'])
        
       # print (HeaderCardIDsofReport)

abcd = dict()
#print (type(files[0]))
HeaderCardIDsofReport = []
ActualDepositID = []

for file_num in range(0,len(files)):
  #  print (file_num)
    path = basepath + '\\' + files[file_num]
 #   print ('path is ',path)
    tree = ET.parse(path)
#    print ('Tree is :',tree)

    root = tree.getroot()
    
    abc(root)
print ('Header Card ID of All Report : ',HeaderCardIDsofReport)
print ('Actual Deposit ID of Reports : ',ActualDepositID)
#print (depIDlist)
headset = set(HeaderCardIDsofReport)
#print ("head", headset)

#print (headset-depset)
#print (depset-headset)

depID_zero = []
for val in depIDlist:
    val = '00'+str(val)
    depID_zero.append(val)
print ("New Deposit ID from Filename : ",depID_zero)

if HeaderCardIDsofReport == depIDlist:
    print ('All Files are equal Header Card ID and Filename ID')
else: 
    print ('All Files are not equal')

if depID_zero == ActualDepositID:
    print ('All Files are equal Deposit ID and Filename ID')
else: 
    print ('All Files are not equal')



