import os
import shutil
import file

# Getting all files in specific directory
oldPath = "./testData/testDir"
newPath = "./testData/newTestDir"
files = []
for (dirPath, dirNames, fileNames) in os.walk(oldPath):
    for fileName in fileNames:
        newFile = file.File(fileName, dirPath)
        files.append(newFile)

# Divide them into categories
categories = {}
for newFile in files:
        extension = newFile.getExtension()

        if not extension in categories:
            categories[extension] = list() # Create new list for files in category
    
        categories[extension].append(newFile)

# Move into separate files
for category in categories:
     newFolder = os.mkdir(f'{newPath}/{category}')
     for newFile in categories[category]:
          shutil.copy(f'{newFile.getPath()}/{newFile.getName()}', f'{newPath}/{category}/{newFile.getName()}') # Copy files from old path to new