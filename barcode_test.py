import os
import re

def getBarCode(input_folder, output_folder):

#open input_folder
	for i in os.listdir(input_folder):
		
		folderName = os.getname(i)
		path1 = "input_folder/%s" %folderName
		fList1 = os.chdir(path1)
		
		#open sub folders
		for x in os.listdir(fList1):
		
			path2 = "input_folder/%s/*.bcl" %folderName
			#read in first line, use wildcard to open only file in folder
			fList2 = open(path2).readline()
		
			#look for barcode
			#split firstline on ":" and use last item in list

			groups = fList2.split(":")
			barcode = groups[-1]
		
			#compare str.barcode to other folders
			#use barcode data to compare to other folders
	
			#if match copy to folder
		
			path3 = "output_folder/%s" %barcode
			if barcode == os.listdir(path3)
			shutil.copytree(path1, path3)
			else 
			#make new folder with name barcode
	
				os.mkdir(path3)
				shutil.copytree(path1, path3)

			
go to next file