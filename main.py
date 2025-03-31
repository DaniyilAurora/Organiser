import os
import shutil
import file

# Getting all files in specific directory
def getFiles(dir: str):
    files = []
    for (dirPath, dirNames, fileNames) in os.walk(dir):
        for fileName in fileNames:
            newFile = file.File(fileName, dirPath)
            files.append(newFile)
    
    return files

# Dividing files into categories
def categoriseFiles(files: list[file.File]):
    categories = {}
    for newFile in files:
            extension = newFile.getExtension()

            if not extension in categories:
                categories[extension] = list() # Create new list for files in category

            categories[extension].append(newFile)
    
    return categories

# Moving files from one folder to another
def moveFiles(categories: dict, newPath: str):
    for category in categories:
        newFolder = os.mkdir(f'{newPath}/{category}')
        for newFile in categories[category]:
            shutil.copy(f'{newFile.getPath()}/{newFile.getName()}', f'{newPath}/{category}/{newFile.getName()}') # Copy files from old path to new


def main():
    files = getFiles("./testData/testDir")
    newPath = "./testData/newTestDir"
    categories = categoriseFiles(files)
    moveFiles(categories, newPath)

main()