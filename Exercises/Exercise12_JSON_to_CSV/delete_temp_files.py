import os

rootdir=r"C:\Users\HUPPE\Desktop\source_output"

## If file exists, delete it ##
#if os.path.isfile(myfile):
#    os.remove(myfile)
#else:    ## Show an error ##
#    print("Error: %s file not found" % myfile)


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith("temp.txt"):
            os.remove(filepath)
