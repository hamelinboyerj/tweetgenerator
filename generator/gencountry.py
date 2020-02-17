import csv
import random
import os





def main():
    usersinfo = open ('../output/usersinfo.csv')
    countriesinfo = open ('../data/original/countriesworld.csv')
    usercountry = open ('../output/usercountry.csv' , "w")

    usersreadercsv = csv.reader(usersinfo, delimiter = ",")
    countriesreadercsv = csv.reader(countriesinfo, delimiter = '\t')

    writer = csv.writer(usercountry)

    countriestuple = tuple(countriesreadercsv)
    countrieslist = [x[0] for x in countriestuple]

    for row in usersreadercsv:
        table_usercountry = [str(row[0])] + [str(random.choice(countrieslist))]
        writer.writerow(table_usercountry)


    usersinfo.close()
    countriesinfo.close()
    usercountry.close()

if __name__=="__main__":
    main()
