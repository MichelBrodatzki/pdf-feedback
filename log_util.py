from datetime import datetime

def log(message):
    print ("[{}] {}".format(datetime.now(), message))

def error(message):
    # TODO (Brodi): Implement better error logging
    log(message)