import io
from configparser import ConfigParser
from unittest import TestCase

# import jsonpath
import requests

import json


# import jsonpath

def get_url(env, key_name):
    parser = ConfigParser()
    parser.read("../environment.ini")
    return parser.get(env, key_name)
    # with open("../environment.ini") as f:
    #     sample_config = f.read()
    # config = ConfigParser.RawConfigParser(allow_no_value=True)
    # config.readfp(io.BytesIO(sample_config))
    # return parser.get(env, key_name)

# API URL
BASE_URL = "http://127.0.0.1:5000"

env = "local"


class TestPostEndPoint(TestCase):
    def test_post_end_point(self):
        # file = open("CreateUser.json", "r")
        # json_input = file.read()
        # request_json = json.loads(json_input)
        get_response = requests.post(get_url(env, "host") + "/api/v1/accounts/post")
        print("==> Status: ", get_response.status_code)
        print("==> Text", get_response.text)
        print("==> headers:", get_response.headers)
        print("========>", get_url(env, "host"))

