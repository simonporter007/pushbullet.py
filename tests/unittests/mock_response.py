from __future__ import print_function
from urlparse import urlparse

import json
import os.path

class MockResponse:
    """
    MockResponse class to store json and status_code response
    to mock requests function.
    """
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def mocked_requests_get(*args, **kwargs):
    """
    Mock get request to return json from file with status 200.
    Will return empty response with 404 if not found.
    """
    response = get_response(args[0])
    if response:
        return MockResponse(response, 200)
    
    return MockResponse({}, 404)

def mocked_requests_post(*args, **kwargs):
    """
    Mock post request to return json from file with status 200.
    Will return empty response with 404 if not found.
    """
    response = get_response(args[0])
    if response:
        payload = json.loads(kwargs["data"])
        for k in payload:
            response[k] = payload[k]
        return MockResponse(response, 200)

    return MockResponse({}, 404)

def get_response(url):
    """
    load json responses from the filesystem based off url.
    """
    parsed_url = urlparse(url)
    with open(os.path.normpath('tests/unittests/resources{0}.json'.format(parsed_url.path))) as json_file:
        return json.load(json_file)