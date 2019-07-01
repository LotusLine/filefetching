import os

#specify path of directory
path = r"/users/azabro/downloads"

#call listdir() method
#path is the directory of that which you want to list
directories = os.scandir(path)

#This will print all the files and directories
for file in directories:
    print(file)
    
#print filenames
with os.scandir(path) as dirs:
    for entry in dirs:
        print(entry.name)
        
        
    
for files in os.listdir(path):
    if os.path.isdir(os.path.join(path, files)):
        print(files)
        
print('Sucessfully completed the directory listing :)')