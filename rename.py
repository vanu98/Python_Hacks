import os

for i,file in enumerate(os.listdir(os.getcwd())):
	os.rename(file,'Image'+"__"+str(i)+".jpg")