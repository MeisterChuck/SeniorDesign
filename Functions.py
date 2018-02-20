import glob
import ntpath
import os


# Used ntpath for program to navigate directories on all platforms
# Used os to get filename
def getfilename(file_path):
    file_path_name = ntpath.basename(file_path)
    file_path_name_split = os.path.splitext(file_path_name)[0]
    file_name = file_path_name_split[:-7]
    return file_name


# Navigate the input data directory and and located all the .gz files with each mental state
def navigate(category):
    index = 0

    for name in glob.glob('Data-I/*' + category + '*/unprocessed/3T/*/*?.gz'):
        index = index + 1
        #print(name)
        print("In {0} - {1}".format(category, getfilename(name)))

    print(f"There are {index} files\n")