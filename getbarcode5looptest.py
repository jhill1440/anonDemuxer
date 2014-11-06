import os
import shutil

def barCode(read1File, read2File, outputFolder):
	
	
	
	R1Temp = open(read1File)
	
	R2Temp = open(read2File)
	
	for line in R1Temp:
	
		tempR1 = line + line + line + line
		print tempR1
	
	return

barCode("/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/data1/lane1_R1_short", "/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/data1/lane1_R2_short", '/Users/joshuahill/Dropbox (TxGen)/Share/Lab/joshtest/out1')

		
			