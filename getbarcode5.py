import os

def barCode(read1File, read2File, outputFolder):
	
	
	R1Temp = open(read1File)
	
	R2Temp = open(read2File)
	
	
	while True:
		
		tempR1 = R1Temp.readline() + R1Temp.readline() + R1Temp.readline() + R1Temp.readline()
	
		tempR2 = R2Temp.readline() + R2Temp.readline() + R2Temp.readline() + R2Temp.readline()
	
		groups = tempR2.split("\n")
		#assign barcode and strip last linebreak
		barcode = groups[1].rstrip()
	
		#change to output directory
		os.chdir(outputFolder)
		
		#write data to file
		desFile = open(barcode, "a")
		desFile.write(tempR1)
		
		
	
	return

barCode("/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/data1/lane1_R1_med.fastq", "/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/data1/lane1_R2_med.fastq", '/Users/joshuahill/Desktop/out1')

		
			
