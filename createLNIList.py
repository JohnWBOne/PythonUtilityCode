from sys import argv
from os import listdir

def processFailedList(failedFileName):
    failedDirList = open(failedFileName)
    lines = failedDirList.readlines()
    failedDirList.close()
    cnt=0
    for aLine in lines:
        theFiles = listdir(aLine.rstrip("\n"))
        for aFile in theFiles:
            corruptedFile = open(aLine.rstrip("\n")+"\\"+aFile);
            corruptedFile.readline()
            corruptedFileContents = corruptedFile.readline()
            corruptedFile.close()
            beginIndex = corruptedFileContents.index("guid:guid=\"urn:contentItem:")+len("guid:guid=\"urn:contentItem:");
            endIndex = beginIndex+28;
            theLNI = corruptedFileContents[beginIndex:endIndex]
            cnt = cnt+1
            print(theLNI)

    print("Total number of lnis",cnt)

if __name__ == "__main__":
    processFailedList(argv[1])