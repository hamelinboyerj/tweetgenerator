import csv
import os
import copy
import random
from io import open

## Similarly as gencountry, we use a counter to count the number of articles
## constructed



def main():
    userid_opener = open ('../output/usersinfo.csv', encoding = 'latin1')
    userid_reader = csv.reader(userid_opener, delimiter = ',')

    article = open ('/home/juleshamelinboyer/nytimesarticle/samplenytimes.csv', encoding='latin1', errors = 'ignore')
    articlecsvreader = csv.reader(article, delimiter = '\t')

    out_file = open ('../output/tweetuser.csv', "w")
    writer = csv.writer(out_file)

    articlelist = list(articlecsvreader)

    for row in userid_reader:
        userid_tweet = [''.join( [str(row[0])] + [str(random.choice(articlelist))] ) ]
        writer.writerow(userid_tweet)

    userid_opener.close()
    article.close()
    out_file.close()


if __name__== "__main__" :
    main()
