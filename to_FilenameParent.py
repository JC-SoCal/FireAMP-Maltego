import sys
from MaltegoTransform import * 
import fa_parser as fa

value = sys.argv[1]

MT = MaltegoTransform()
MT.parseArguments(sys.argv)

#########################################
## lookup fieldname of sending request ##
#########################################
field = None
filepath = None
for x in MT.values:

	if x == 'properties.fabaseentity': continue
	if x.startswith('properties.'):
		field = fa.fieldLookup(x)
	if x.startswith('CSV File'):
		filepath = MT.values[x].replace("\\\\", "\\")

#############################
## Get the correlated data ##
#############################
data = fa.parseCSV(filepath)
query = fa.correlate(data, field, value)
result = fa.ItemsCounts(query, 'Filename (Parent)') ## Edit Here

####################
## Submit Results ##
####################
for entry in result:
	e = MT.addEntity("jc.FilenameParent",entry); ## Edit HEre
	e.addAdditionalFields("CSV File",filepath,True,filepath)
MT.returnOutput()