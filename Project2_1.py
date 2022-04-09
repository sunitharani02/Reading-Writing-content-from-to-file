#import the csv module
import csv

#open csv file
file = open("example.csv", "r")

#read the csv file
rdr = csv.reader(file, delimiter=",")

#output csv content
for row in rdr:
    if row[3] == "IT":
        print(row)

#close the csv
file.close()
