#!/usr/bin/env python

import requests
import random
import time
import base64

from requests_oauthlib import OAuth2Session

class Request():

    def __init__(self, url, key, secret):
        self.url = url + "%s"
        self.key = key
        self.secret = secret
        self.athena = OAuth2Session(key, token=secret)

    def set_access_token(self, access_token):
        self.access_token = access_token

    def make(self, req_type, url, args):
        try:
            if "headers" not in args: args["headers"] = None
            if "data" not in args: args["data"] = None
            if "json" not in args: args["json"] = None
            if "files" not in args: args["files"] = None

            req = getattr(self.athena, req_type)
            print("Made request")
            res = req(self.url % url, headers=args["headers"], data=args["data"], json=args["json"], files=args["files"])
            print("RESPOSNE")
            print(res)
            return res

        except AttributeError:
            print("Incorrect request type! Fix it.")
            exit(0)
