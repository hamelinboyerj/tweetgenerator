import unittest
import os
import csv
import sys
import unittest

sys.path.append('../generator')



def get_config():
    config = {}
    config['firstname_path'] = './data/firstname.txt'
    config['lastname_path'] = './data/lastname.txt'
    return config

def get_newfirstname() :
    firstname = {}
    firstname['firstname_path'] = './data/original/firstname.txt'
    return firstname

def get_username():
    username = {}
    username['username_path'] = '../output/usersinfo.csv'

def get_newtweet() :
    newtweet = {}
    newtweet['newtweet_path'] = './data/tweetuser.csv'
    return newtweet
