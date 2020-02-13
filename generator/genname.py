import csv
import random
import os
import string



## Opening data files, and csv reader/writer initialisation

random.seed(314)
name = open ('../data/original/names.csv')
usersinfo = open ('../output/usersinfo.csv' , "w")
readnames = csv.reader(name, delimiter = '\t')
writenames = csv.writer(usersinfo)
numberofusers = int(input('How many users do you want to generate ? '))

def main():
##Define the table usersID
    def createuser():
        ##Create the row userID
            new_row_ID = [''.join( [row[0],row[1]] + [str(random.randint(1,9))] + [str(random.randint(1,9))])  ]
            ##Generate age based on average Twitter user age (30)
            new_row_ID_age = [new_row_ID[0]] + [str(round(random.gauss(30,5)))]
            ## Generate random email address based on user ID
            email_list = ["@gmail.com","@outlook.com","@yahoo.com"]
            new_row_ID_age_email = [','.join([new_row_ID_age[0]] + [new_row_ID_age[1]] + [ ''.join([new_row_ID_age[0]] + [str(random.choice(email_list))])])]
            writenames.writerow(new_row_ID_age_email)
            return;

            ## Implementation of the counter
            # while counter < numberofusers:
    for row in readnames:
        createuser()
        # counter = counter + 1

if __name__== "__main__" :
    main()

usersinfo.close()
name.close()
