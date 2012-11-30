__author__ = 'Colin'

# Should support gathers from various apps: SMS linked to a web url, direct XMPP, direct Twitter, etc
# each scatter/gather plugin should be its own class, this module will simply handle the timing and tracking
# of who should be asked questions, then call the appropriate ask method on a plugin (probably at random).

import twitter
import sys
import yaml

# local packages
import Store

# default data gathering plugins - these will be separate classes eventually
twitter_enabled = False
xmpp_enabled = False
stdin_enabled = True

def xmpp_setup():
    xmpp_file = r'../xmpp_config.yaml'
    xmpp_config = yaml.load(file(xmpp_file))
    return xmpp_config

def twitter_setup():
    twitter_file = r'../twitter_config.yaml'
    twitter_config = yaml.load(file(twitter_file))
    twApi = twitter.Api(
        consumer_secret='uS5rmkfJnSellX4a0j5hWNzSmjJjZsVM7HMq4AWZXx8',
        consumer_key=twitter_config['consumer_key'],
        access_token_key=twitter_config['access_token_key'],
        access_token_secret=twitter_config['access_token_secret'],
        debugHTTP=True
    )
    return twApi

def stdin_setup():
    '''
     Prepare stdin to be read from
    '''


twApi = None
xmpp_config = None

if twitter_enabled:
    twApi = twitter_setup()

if xmpp_enabled:
    xmpp_config = xmpp_setup()

if stdin_enabled:
    stdin_setup()

def ask_question():
    name = 'Colin'

    questions = Store.getQuestions()

    for q in questions:
        print str(q) + ": " + questions[q]
        input = sys.stdin.readline()
        input = int(input)
        print "You said " + str(input) + ". Saved? " + str(Store.storeResult(name=name,score=input,question_id=q))
        print "----------------"


    print "Thanks!! You've answered all the questions for now."

