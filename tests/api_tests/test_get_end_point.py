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


class TestGetEndPoint(TestCase):
    def test_get_end_point_all(self):
        get_response = requests.get(get_url(env, "host") + "/api/v1/resources/accounts/all")
        #print("1==> Status: ", get_response.status_code)
        #assert(get_response.status_code == 201)
        # print("==> Text", get_response.text)
        # print("==> headers:", get_response.headers)
        #print("========>", get_url(env, "host"))
        self.assertEqual(200, get_response.status_code)


    def test_get_end_point_id(self):
        get_response = requests.get(get_url(env, "host") + "/api/v1/accounts?id=1")
        print("2==> Status: ", get_response.status_code)
        assert (get_response.status_code == 200)
        # print("==> Text", get_response.text)
        # print("==> headers:", get_response.headers)
        #print("========>", get_url(env, "host"))
        self.assertEqual(200, get_response.status_code)
