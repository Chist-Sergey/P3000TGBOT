# thanks to Tiago Coutinho for this solution
# https://stackoverflow.com/questions/6234405/logging-uncaught-exceptions-in-python#16993115

import logging
import traceback


def logger(*info):
    text = ''.join(traceback.format_exception(*info()))
    logging.error('Unhandled exception: %s', text)
    open('log.txt', 'a').write(text)
