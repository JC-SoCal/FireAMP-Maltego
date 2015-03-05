import csv
import sys

def parseCSV(filepath):
	data = []
	header = None

	with open(filepath, 'rb') as csvfile:
		filereader = csv.reader(csvfile, delimiter=',')
		for row in filereader:

			if header == None: 
				header = row #set header
				continue

			entry  = {}
			for i in range(len(header)):
				entry[header[i]] = row[i]

			data.append(entry)

	return data

def ItemsCounts(data, ColName):
	items = {}
	for entry in data:
		if entry[ColName] == '': continue # get rid of blank lines
		if entry[ColName] in items.keys():
			items[entry[ColName]] += 1
		else:
			items[entry[ColName]] = 1
	return items

def correlate(data, ColName, term):
	items = []
	for entry in data:
		if entry[ColName] == term:
			items.append(entry)
	return items

def fieldLookup(value):
	data = {
			'properties.md5detection':'MD5 (Detection)',
			'properties.filenameparent':'Filename (Parent)',
			'properties.filepath':'Filepath',
			'properties.remoteip':'Remote IP',
			'properties.ip':'IP',
			'properties.filename':'File Name',
			'properties.hostname':'Hostname',
			'properties.shaparent':'SHA-1 (Parent)',
			'properties.detectionname':'Detection Name',
			'properties.url':'URL',
			'properties.md5parent':'MD5 (Parent)',
			'properties.sha-256detection':'SHA-256 (Detection)',
			'properties.sha-256parent':'SHA-256 (Parent)',
			'properties.time':'Time',
			'properties.eventtype':'Event Type',
			'properties.sha1detection':'SHA-1 (Detection)',
			'properties.port':'Port'
	}
	return data[value]
	
