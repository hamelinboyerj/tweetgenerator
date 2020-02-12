import unittest
import os
import csv


def get_config():
    config = {}
    config['firstname_path'] = './data/firstname.txt'
    config['lastname_path'] = './data/lastname.txt'
    return config

def get_newfirstname() :
    firstname = {}
    firstname['firstname_path'] = './data/original/firstname.txt'
    return firstname

def get_newlastname():
    lastname = {}
    lastname['lastname_path'] = './data/original/lastname.txt'
    return lastname

def get_newtweet() :
    newtweet = {}
    newtweet['newtweet_path'] = './data/tweetuser.csv'
    return newtweet
