#import the csv module
import csv

#new record
newRec = ["1005", "Patrick", "Marleau", "IT"]

#open csv in append mode
file = open("example.csv", "a")

#write to the csv file
wrt = csv.writer(file)

#write the new record into the csv file
wrt.writerow(newRec)

#close the csv file
file.close()
