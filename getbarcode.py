import os
import shutil



inputFolder = "data1"

path1 = "%s/" %inputFolder
fList1 = os.listdir(path1)

os.chdir(path1)


folderName2 = 'data2'

path2 = "%s/test1.txt" %folderName2

#read in first line, use wildcard to open only file in folder
fList2 = open(path2).readline()
		
#look for barcode
#split firstline on ":" and use last item in list

groups = fList2.split(":")
barcode = groups[-1]


#os.chdir("/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/out1")
#os.mkdir(barcode)
#shutil.copytree(path3/folderName2, barcode)

print groups
print barcode
print os.getcwd()
	
		
			