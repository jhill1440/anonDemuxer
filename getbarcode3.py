import os
import shutil

def barCode(inputFolder, outputFolder):

	#make a path for the folder
	path1 = "%s/" % inputFolder
	
	#list all things in path1
	fList1 = os.listdir(path1)
	
	#change to path1
	os.chdir(path1)

	#temp folder name
	folderName2 = 'data2'
	#path for temp folder
	path2 = "%s/test1.txt" % folderName2

	#read in first line, use wildcard to open only file in folder
	fList2 = open(path2).readline()
		
	#look for barcode
	#split firstline on ":" and use last item in list

	groups = fList2.split(":")
	#assign barcode and strip last linebreak
	barcode = groups[-1].rstrip()
	#is it working
	print barcode

	#assign paths for copying
	path4 = '/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/data1/data2/test1.txt'
	path5 = outputFolder + '/%s/%s' % (barcode, folderName2)
	
	#change to output directory and make sub folders
	os.chdir(outputFolder)
	os.mkdir(barcode)
	os.chdir(outputFolder + "/" + barcode)
	os.mkdir(folderName2)
	
	#copy file to correct barcode file
	shutil.copy(path4, path5)
	
	return

barCode("data1", '/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/out1')

		
			