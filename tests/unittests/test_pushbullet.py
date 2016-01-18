from urlparse import urlparse
import mock
import json
import os.path

from pushbullet import pushbullet

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def mocked_requests_get(*args, **kwargs):
    if args[0] == 'https://api.pushbullet.com/v2/devices':
        return MockResponse({
  "devices": [
    {
      "active": True,
      "app_version": 8623,
      "created": 1.412047948579029e+09,
      "iden": "xxxxxxxxxxxxxxxxxxxxxxxx",
      "manufacturer": "Apple",
      "model": "iPhone 5s (GSM)",
      "modified": 1.412047948579031e+09,
      "nickname": "Elon Musk's iPhone",
      "push_token": "production:f73be0ee7877c8c7fa69b1468cde764f"
    }
  ]
}, 200)
    else:
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse({}, 404)

def mocked_requests_post(*args, **kwargs):
    if args[0] == 'https://api.pushbullet.com/v2/devices/xxxxxxxxxxxxxxxxxxxxxxxx':
        resp = {
      "active": True,
      "app_version": 8623,
      "created": 1.412047948579029e+09,
      "iden": "ujpah72o0sjAoRtnM0jc",
      "manufacturer": "Apple",
      "model": "iPhone 5s (GSM)",
      "modified": 1.412047948579031e+09,
      "nickname": "Elon Musk's iPhone",
      "push_token": "production:f73be0ee7877c8c7fa69b1468cde764f"
    }
        payload = json.loads(kwargs["data"])
        for k in payload:
            resp[k] = payload[k]
        return MockResponse(resp, 200)
    else:
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse({}, 404)

def get_response(*args, **kwargs):
    """
    A stub requests get() implementation that load json responses from
    the filesystem.
    """
    for arg in args:
        print arg
    #parsed_url = urlparse(url)
    #resource_file = os.path.normpath('tests/unittests/resources{0}'.format(parsed_url.path))
    #return open(resource_file, mode='rb')
    return True
    
@mock.patch('pushbullet.pushbullet.requests.Session.get', side_effect=mocked_requests_get)
@mock.patch('pushbullet.pushbullet.requests.Session.post', side_effect=mocked_requests_post)
class TestPushbullet(object):
        
    def test_edit_device_without_nickname(self, mock_get, mock_post):
        pb = pushbullet.Pushbullet("API_KEY")
        device = pb.devices[0]
        new_device = pb.edit_device(device)
        assert new_device.nickname == device.nickname
        