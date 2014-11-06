import os
import shutil

def barCode(inputFolder, outputFolder):
	
	dirList1 = os.listdir(inputFolder)
	
	print dirList1
	
	for i in dirList1:
	
		if os.path.isfile(i) == 0:
			
			dirName1 = os.path.abspath(inputFolder + "/" + i)
			
			os.chdir(dirName1)
			
			fList2 = open("test1.txt").readline()
			
			groups = fList2.split(":")
			#assign barcode and strip last linebreak
			barcode = groups[-1].rstrip()
			#is it working
			print barcode
			
			#change to output directory and make sub folders
			os.chdir(outputFolder)
			os.mkdir(barcode)
			os.chdir(outputFolder + "/" + barcode)
			os.mkdir(i)
			
			#shutil.copy()
			
		else:
			pass
			
		
		#list all things in path1
		#fList1 = os.listdir(inputFolder)
		
		#print os.getcwd()
		
		#change to path1
			#os.chdir(dirName1)
			#print os.getcwd()
		#temp folder name
		#folderName2 = 'data2_1'
		#path for temp folder
			#path2 = "%s/test1.txt" % (dirName1)

		#read in first line, use wildcard to open only file in folder
			#fList2 = open(path2).readline()
			#print fList2
		#look for barcode
		#split firstline on ":" and use last item in list

		#groups = fList2.split(":")
		#assign barcode and strip last linebreak
		#barcode = groups[-1].rstrip()
		#is it working
		#print barcode
			
		
		#assign paths for copying
		#path4 = '/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/data1/data2/test1.txt'
		#path5 = outputFolder + '/%s/%s' % (barcode, folderName2)
	
		#change to output directory and make sub folders
		#os.chdir(outputFolder)
		#os.mkdir(barcode)
		#os.chdir(outputFolder + "/" + barcode)
		#os.mkdir(folderName2)
	
		#copy file to correct barcode file
		#shutil.copy(path4, path5)
		
	return

barCode("/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/data1/", '/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/out1')

		
			