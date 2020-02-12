import csv
import os
import tempfile

namelist = open ('../data/names.csv')
article = open ('/home/juleshamelinboyer/nytimesarticle/nytimesarticle.csv')
out_file = open ('../data/tweetuser.csv', "w")
nameread = namelist.readlines()
articleread = article.readlines()
writer = csv.writer(out_file, delimiter= ',')
## Similarly as gencountry, we use a counter to count the number of articles
## constructed
i = 1
while i < len(nameread):
        for row in zip(nameread, articleread):
            writer.writerow(row)
            i += 1
            print(i)
close(namelist)
close(article)
close(out_file)
