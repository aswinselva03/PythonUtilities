'''
This program renames a list of files placed in a directory based on the file created date. 
i.e. the iterator will start with the file thiat is created first and rename subsequently
'''
import os

dir = "D:\\Aswin\\RenameMe\\" #the directory in which the files are placed goes here
filenames = os.listdir(dir) 
filenames = [file for file in filenames if os.path.isfile(os.path.join(dir,file))] #ignoring other folders placed in the directory

sorted_filenames = sorted(filenames, key = lambda x: os.path.getctime(dir+x)) #sorting the files based on created epoch time
#renaming the files        
for filename,i in zip(sorted_filenames, range(len(sorted_filenames))):
    if os.path.isfile(os.path.join(dir,filename)):
        os.rename(dir+filename, dir+"renamed"+str(i)+".txt")
    else:
        print(filename)
        continue
    
