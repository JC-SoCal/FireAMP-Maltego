import sys
from MaltegoTransform import * 
import fa_parser as fa

column = sys.argv[1]
filepath = sys.argv[2]

MT = MaltegoTransform()
data = fa.parseCSV(filepath)

##########################################################################
if column == 'MD5 (Detection)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.MD5Detection",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Filename (Parent)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.FilenameParent",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Filepath':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.Filepath",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Remote IP':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.RemoteIP",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'IP':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.ip",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'File Name':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.filename",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Hostname':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.Hostname",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'SHA-1 (Parent)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.SHA-1Parent",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Detection Name':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.DetectionName",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'URL':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.URL",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'MD5 (Parent)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.MD5Parent",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'SHA-256 (Detection)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.SHA-256Detection",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'SHA-256 (Parent)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.SHA-256Parent",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Time':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.Time",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Event Type':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.EventType",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'SHA-1 (Detection)':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.SHA-1Detection",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################
elif column == 'Port':
	result = fa.ItemsCounts(data, column)
	for entry in result:
		e = MT.addEntity("jc.Port",entry);
		e.addAdditionalFields("CSV File",filepath,True,filepath)
##########################################################################

MT.returnOutput()
