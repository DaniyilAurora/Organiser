class File():
    def __init__(self, fileName: str, filePath: str):
        self.fileName = fileName
        self.filePath = filePath.replace("\\", "/") # To make directory valid
        self.extension = fileName.split(".")
        self.extension = self.extension[len(self.extension) - 1] # Get file extension
    
    def getName(self):
        return self.fileName
    def getPath(self):
        return self.filePath
    def getExtension(self):
        return self.extension
    def __str__(self):
        return (f'FileName: {self.fileName}, Extension: {self.extension}, FilePath: {self.filePath}')
