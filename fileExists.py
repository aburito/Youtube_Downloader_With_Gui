import os

# Path
path = 'C:/Users/drochette/PycharmProjects/Youtube_Downloader/Videos/Oil Pan removal by Dealership  GR86.mp4'

# Check whether a path pointing to a file
isFile = os.path.isfile(path)
print(isFile)

# Path
path = '/home/User/Desktop/'

# Check whether the path is a file
isFile = os.path.isfile(path)
print(isFile)