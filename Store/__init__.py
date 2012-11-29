from couchdb import PreconditionFailed

__author__ = 'Colin'

import couchdb
import time
import sys

questions = {
    0: "On a scale of 1 to 5, how good do you feel right now?",
    1: "On a scale of 1 to 5, how satisfied are you with your job?"
    }

def setup_storage():
    couch = couchdb.Server() # defaults to localhost
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

def storeResult(name,question_id,score):
    '''
     Stores a result previously gathered.
    '''
    #TODO: stub
    print >> sys.stderr, "Would have stored " + str(score) + " for question " + str(question_id) + " asked to " + str(name)

    doc = { 'name': str(name), 'timestamp': int(time.mktime(time.gmtime())), 'question_id': 0, 'score': int(score) }
    doc_id, doc_rev = db.save(doc)

    print >> sys.stderr, [doc_id, doc_rev]

    return True


db = setup_storage()
