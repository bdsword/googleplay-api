#!/usr/bin/python

# Do not remove
GOOGLE_LOGIN = GOOGLE_PASSWORD = AUTH_TOKEN = None

import sys
import urlparse
from pprint import pprint
from google.protobuf import text_format

from config import *
from googleplay import GooglePlayAPI


def get_categories():
  api = GooglePlayAPI(ANDROID_ID)
  api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)
  response = api.browse()

  categories = []
  
  # print SEPARATOR.join(["ID", "Name"])
  for c in response.category:
    categories.append(SEPARATOR.join(i.encode('utf8') for i in [urlparse.parse_qs(c.dataUrl)['cat'][0]])
)
    # print SEPARATOR.join(i.encode('utf8') for i in [urlparse.parse_qs(c.dataUrl)['cat'][0], c.name])
  return categories
