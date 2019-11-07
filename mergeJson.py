import json
from collections import defaultdict
import glob
import os
import re



class mergeJsonFiles:
	def __atoi(self, text):
		return int(text) if text.isdigit() else text

	def __natural_keys(self, text):
		return [ self.__atoi(c) for c in re.split(r'(\d+)', text) ]
	
	def mergeJson(self, folderPath, baseInFile, baseOutFile, maxFileSize):
		res  = defaultdict(list)
		os.chdir(folderPath)
		
		size = 0
		counter = 1
		fileNames = glob.glob(baseInFile +'*.json')
		fileNames.sort(key=self.__natural_keys)
		for data_file in fileNames:
			with open(data_file) as json_file:
				currSize = os.path.getsize(data_file)
				
				if size+currSize > maxFileSize:
					outputFile = baseOutFile + str(counter) + '.json'
					with open(outputFile, "w") as outfile:
						json.dump(res, outfile)
					counter+=1
					res = defaultdict(list)
					size=0
				data = json.load(json_file)
				for (key,val) in data.items():
					res[key].extend(val)
				size+=currSize
				
		if(res):
			outputFile = baseOutFile + str(counter) + '.json'
			with open(outputFile, "w") as outfile:
				json.dump(res, outfile)  