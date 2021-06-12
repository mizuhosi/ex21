import os
import sys

def getDirSize(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += getDirSize(entry.path)
    return total


def scanDirSize(path):
    filesAndDirs = os.listdir(path)
    subDirs = [os.path.join(path, f) for f in filesAndDirs if os.path.isdir(os.path.join(path, f))]
    files = [os.path.join(path, f) for f in filesAndDirs if os.path.isfile(os.path.join(path, f))]

    sumSize = 0 
    for folder in subDirs:
        sizeGb = getDirSize(folder) / 1000 / 1000 / 1000
        print("D %s, %.2f" % (folder, sizeGb))
        sumSize += sizeGb
    for file in files:
        sizeGb = os.path.getsize(file) / 1000 / 1000 / 1000
        print("F  %s, %.2f" % (file, sizeGb))
        sumSize += sizeGb


if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) == 2:
        if not os.path.esxists(argvs[1]):
            print("Input path is not exist.")
        else:
            scanDirSize(argvs[1])
    else:
        scanDirSize('.')
