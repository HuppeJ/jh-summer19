import os, csv, json, sys

rootdir=r"C:\Users\HUPPE\Desktop\test_to_csv"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        fileInput = subdir + os.sep + file
        if fileInput.endswith(".json"):
            fileOutput = fileInput[:-4] + "csv"
            inputFile = open(fileInput) #open json file
            outputFile = open(fileOutput, 'w', encoding="utf-8", newline='') #load csv file
            data = json.load(inputFile) #load json content
            inputFile.close() #close the input file
            output = csv.writer(outputFile) #create a csv.write
            output.writerow(data[0].keys())  # header row
            for row in data:
                output.writerow(row.values()) #values row