import csv
import random
import os

usersinfo = open ('../output/usersinfo.csv')
countriesinfo = open ('../data/original/countriesworld.csv')
usercountry = open ('../output/usercountry.csv' , "w")

usersreader = csv.reader(usersinfo, delimiter = ',', quotechar='|')
countriesreadercsv = csv.reader(countriesinfo, delimiter = '\t')
writer = csv.writer(usercountry)
countrieslist = list(countriesreadercsv)

def main():
    for row in usersreader:
        table_usercountry = [row[0]] + [str(random.choice(countrieslist))]
        writer.writerow(table_usercountry)

usersinfo.close()
countriesinfo.close()
usercountry.close()

if __name__=="__main__":
    main()
