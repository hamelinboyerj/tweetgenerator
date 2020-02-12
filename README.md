# tweetgen

The goal of this program is to generate fictionnals tweets content, username, country and hashtags.
The method will be described below.

## Getting started

### Installation

To install the package, you need to launch the setup.py script using Python3.X
Compatibility with Python2.X is not supported.

## Generated datasets

- categories
  - name(id)
  - title
- countries
  - name: Full name
  - country_code(id)
- tags: Tags refenrenced accross multiple tweets
  - name(id): tag identifier
- tweets
  - creation_date(id[2])
  - location
  - category
  - tags
  - user(id[1])
- users
  - username(id)
  - age
  - email


## Main steps

1. `cache.py`: Download the usernames, firstnames and countries dataset
2. `content_to_tweets.py`: Break up article into tweets in the form of tupples [category, date, text]
3. `generate.py {dataset}`: Generate the datasets

## 1st step : genname.py

It generate a dataset of names with user properties such as its `firstname` and `lastname`. By default, the generated datateset is stored in the `names.csv` file.

Actually, the list is matching one first name and one last name in alphabetical order. Given time, we would like to :
- Randomize the matching between firstnames and lastnames.
- add 4 random numbers to the names.csvto give a more realistic idea for a username.

## 2nd step : gencountry.py

Select a random country for each username generated in the first step.

TODO
- data separated by comma
Given time, we would like to :
- select a country for each user based on the density of global world population per country.
- update so that no header files names and country

## 3rd step : gentweet.py

## 4th step : genhashtags.py

Look for the most recurring word in the article and append it to the corresponding tweet content.

TODO
- case sensitive when building inverted index
- plurial worlds to be put singulars
- stop world
- même champ lexical


## 5th step : main.py

Create a final table with the tweeter username, the country of the user,the tweet content and the matching hashtag.


## Developer information

Test are written with [unittest](https://docs.python.org/3/library/unittest.html) and are executed with the command:

```
python test/test.py
```

I) What I want for username.py generator :

1) UsernameID
  - Possibility to choose the number of user to generated : command -h [generate 2K users]
      How to achieve it :
        Create a program that will:
            -create a loop that randomizes the matching between last and first name until number of users is reached.
              -in that loop, append 4 random numbers
              - check for unicity of the UsernameID.

2) Age
    - Randomly assign an age (15-45) to each user
    use a normal distribution

3) Email
    -


FINAL : tweet.py générator//
    - Let people generate tweet in a meaningful way/ predict human tweet generation? which criteria to use for this ?
        For age in tweet : based on average country + normal distribution
        For country of tweet location : based on density of population + normal distribution
          - need a list of country.
