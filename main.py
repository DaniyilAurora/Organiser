import os
import shutil
import file
import datetime

# Getting all files in specific directory
def getFiles(dir: str):
    files = []
    for (dirPath, dirNames, fileNames) in os.walk(dir):
        for fileName in fileNames:
            if not dirPath[len(dirPath) - 1] == "/":
                dirPath = dirPath + "/"  # Add symbol '/' at the end of the path

            newFile = file.File(fileName, dirPath)
            files.append(newFile)

    return files


# Dividing files into categories by their filetype
def categoriseFilesByType(files: list[file.File]):
    categories = {}
    for newFile in files:
            extension = newFile.getExtension()  # Get file creation date

            if extension not in categories:
                categories[extension] = list()  # Create new list for files in category

            categories[extension].append(newFile)  # Add file to specific category

    return categories


# Dividing files into categories by their date of creation
def categoriseFilesByDate(files: list[file.File]):
    categories = {}

    for newFile in files:
        creationDate = os.path.getctime(newFile.filePath + newFile.fileName)  # Get file creation time
        creationDate = datetime.datetime.fromtimestamp(creationDate)

        if not f'{creationDate.day}.{creationDate.month}.{creationDate.year}' in categories:
            categories[f'{creationDate.day}.{creationDate.month}.{creationDate.year}'] = list()  # Create new list for files in category

        categories[f'{creationDate.day}.{creationDate.month}.{creationDate.year}'].append(newFile)  # Add file to specific category

    return categories


# Moving files from one folder to another
def moveFiles(categories: dict, newPath: str):
    for category in categories:
        newFolder = os.mkdir(f'{newPath}/{category}')
        for newFile in categories[category]:
            shutil.copy(f'{newFile.getPath()}/{newFile.getName()}', f'{newPath}/{category}/{newFile.getName()}')  # Copy files from old path to new


def main():
    files = getFiles("./testData/testDir")
    newPath = "./testData/newTestDir"
    categories = categoriseFilesByDate(files)
    moveFiles(categories, newPath)


main()
