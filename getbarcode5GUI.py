import os
import Tkinter, tkFileDialog, tkMessageBox


top = Tkinter.Tk()

root = Tkinter.Tk()
root.withdraw()

def getR1():
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')

def getR2():
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')

def output():
	dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')

R1 = Tkinter.Button(top, text ='Choose R1', command = getR1)
R2 = Tkinter.Button(top, text ='Choose R2', command = getR2)
outDir = Tkinter.Button(top, text ='Choose output Directory', command = output)

"""
if file != None:
    data = file.read()
    file.close()
    print "I got %d bytes from this file." % len(data)
"""    
R1.pack()
R2.pack()
outDir.pack()
top.mainloop()
    
"""
def barCode(read1File, read2File, outputFolder):
	
	
	R1Temp = open(read1File)
	
	R2Temp = open(read2File)
	count = 1000000
	
	while count > 0:
		
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
		count = count - 1
		
	
	return
"""

