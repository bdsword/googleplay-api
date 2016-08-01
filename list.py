#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import sys
from pprint import pprint

from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt, print_header_line, print_result_line, get_parsed_result


def list(cat, ctr = None, nb_results = None, offset = None):
    api = GooglePlayAPI(ANDROID_ID)
    api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)
    try:
        message = api.list(cat, ctr, nb_results, offset)
    except:
        print "Error: HTTP 500 - one of the provided parameters is invalid"

    if (ctr is None):
        print SEPARATOR.join(["Subcategory ID", "Name"])
        for doc in message.doc:
            print SEPARATOR.join([doc.docid.encode('utf8'), doc.title.encode('utf8')])
    else:
        print_header_line()
        doc = message.doc[0]
        results = []
        for c in doc.child:
            results.append(get_parsed_result(c))
        return results
