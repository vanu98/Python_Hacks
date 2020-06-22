import os

for subdir, dirs, files in os.walk('e:'):
	for file in files:
		if(file=='lala.txt'):
			print(os.path.join(subdir, file))
			break
