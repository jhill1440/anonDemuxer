import os
from itertools import izip, imap
import operator


fList = os.listdir('/Users/joshuahill/Desktop/out1')

fList1 = fList[1::]

#testSequence = fList1[0]


#print fList1
#print testSequence

for i in fList1:

	testSequence = i
	
	
	for x in fList1:
	
		#assert len(testSequence) == len(i)
		distance = sum(c1 != c2 for c1, c2 in izip(testSequence, x))
		
		if distance == 1:
			os.chdir('/Users/joshuahill/Desktop/out1')
			targetFile = open(x, "a")
			testSequenceOpen = open(testSequence)
			testSequenceFile = testSequenceOpen.read()
			targetFile.write(testSequenceFile)
			
			os.remove(testSequence)
		
		#print distance
	
	
	
	
	

		

	


"""
def hamming(str1, str2):
    #hamming1(str1, str2): Hamming distance. Count the number of differences
    #between equal length strings str1 and str2.
    # Do not use Psyco
    assert len(str1) == len(str2)
    print sum(c1 != c2 for c1, c2 in izip(str1, str2))
    
hamming('NAACAGCG', 'NAACATCG')
"""
