
__author__ = 'Colin'

import couchdb
import time
import sys
import yaml
import datetime

from couchdb import PreconditionFailed
from couchdb.client import Server, Document
from couchdb.mapping import TextField, DateTimeField, IntegerField


# object representing a single question asked
class Result(Document):
   name = TextField()
   question = TextField()
   score = IntegerField()
   added = DateTimeField(default=datetime.datetime.now())


class Question:
    longtext = ""
    shorttext = ""
    minscore = 1
    maxscore = 5
    question_id = 0


questions = [
    Question(
        longtext = "On a scale of 1 to 5, how good do you feel right now?",
        shorttext = "feel",
        minscore = 1,
        maxscore = 5,
        question_id = 1
        ),
    Question(
        longtext = "On a scale of 1 to 5, how satisfied are you with your job?"
        shorttext = "job",
        minscore: 1,
        maxscore: 5,
    )
]


def setup_storage():
    storage_config = yaml.load(file("storage_config.yaml"))
    couch = couchdb.Server("http://" + storage_config['couchdb_hostname'] + ":5984") # defaults to localhost
    #TODO: support couch running somewhere else

    db = None
    try:
        db = couch.create('moodlooker-answers')
    except PreconditionFailed:
        db = couch['moodlooker-answers']

    if db == None:
        raise ValueError

    return db


def getQuestions():
    # TODO: stub
    return questions

def getResult(name,question_id):
    # TODO: stub
    return {}

def getResultsForUser(name):
    # TODO: stub
    return {}

def storeResult(name,question_id,score):
    '''
     Stores a result previously gathered.
    '''
    #TODO: stub
    print >> sys.stderr, "Would have stored " + str(score) + " for question " + str(question_id) + " asked to " + str(name)

    result = Result()
    result['name'] = name
    result['question'] = questions[question_id]
    result['score'] = score
    db.save(result)

    print >> sys.stderr, result

    return True

db = setup_storage()
