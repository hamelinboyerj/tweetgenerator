import csv
import random
import os
import string

random.seed(314)
name = open ('../data/original/names.csv')
usersinfo = open ('../output/usersinfo.csv' , "w")

# numberofuser = int(input('How many users do you want to generate ? '))
readnames = csv.reader(name, delimiter = '\t')
writenames = csv.writer(usersinfo)

##Create the table userID
for row in readnames:
    ##Create the row userID
    new_row_ID = [''.join([row[0],row[1]] + [str(random.randint(1,9))] + [str(random.randint(1,9))])  ]
    ##Generate age based on average Twitter user age (30)
    new_row_ID_age = [new_row_ID[0]] + [str(round(random.gauss(30,5)))]
    ## Generate random email address based on user ID
    email_list = ["@gmail.com","@outlook.com","@yahoo.com"]
    new_row_ID_age_email = [','.join([new_row_ID_age[0]] + [new_row_ID_age[1]] + [ ''.join([new_row_ID_age[0]] + [str(random.choice(email_list))])])]
    writenames.writerow(new_row_ID_age_email)

usersinfo.close()
name.close()
