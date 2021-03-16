#import xml.etree.ElementTree as ET

from xml.etree import ElementTree as etree

data = '''
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<BPS Created="2021-02-05 20:45:27">
<Machine SerialNumber="201201" Site="" DPRelease="105.3" SoftwareRelease="4.2.2" VersionInfo="" Name="520ST48602" Type="BPS C5">
<Expected Currency="MIX" Value="0" />
<ParameterSection Number="19" StartTime="2021-02-05 19:42:20" EndTime="" opmodename="MixHDP">
<Operator>12590</Operator>
<HeadercardUnit HeaderCardID="51859930" DepositID="0051859930" denomvalue="100" DeclaredDepositAmount="0" Currency="MIX" StartTime="2021-02-05 20:15:58" MilliSec="1" EndTime="2021-02-05 20:45:27" Rejects="YES">
<Counter Currency="INR" DenomID="17473" Value="10" Quality="Acc" Issue="C" Output="Stacked" Number="2" />
<Counter Currency="INR" DenomID="17507" Value="50" Quality="Acc" Issue="E" Output="Stacked" Number="1" />
</HeadercardUnit>
</ParameterSection>
</Machine>
</BPS>
'''

tree = etree.fromstring(data)
print(tree.items())
#print (dir(tree))
'''
print (tree.find('Machine').get('SerialNumber'))
print (tree.find('Machine').get('DPRelease'))
print (tree.find('Machine').get('SoftwareRelease'))
print (tree.find('Machine').get('VersionInfo'))
print (tree.find('Machine').get('Name'))
print (tree.find('Machine').get('Site'))
print (tree.find('Machine').get('Type'))

print (tree.find('Expected').get('Currency'))
print (tree.find('Expected').get('Value'))
print (tree.find('HeadercardUnit').get('HeaderCardID'))


'''