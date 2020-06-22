#Code to rename all images in a folder
import os
os.chdir('enter path to folder')
for i,file in enumerate(os.listdir(os.getcwd())):
	os.rename(file,'Image'+"__"+str(i)+".jpg")
