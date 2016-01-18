import mock
from pushbullet import pushbullet
from mock_response import mocked_requests_get, mocked_requests_post
    
@mock.patch('pushbullet.pushbullet.requests.Session.get', side_effect=mocked_requests_get)
@mock.patch('pushbullet.pushbullet.requests.Session.post', side_effect=mocked_requests_post)
class TestPushbullet(object):
        
    def test_edit_device_without_nickname(self, mock_get, mock_post):
        pb = pushbullet.Pushbullet("API_KEY")
        device = pb.devices[0]
        new_device = pb.edit_device(device)
        assert new_device.nickname == device.nickname
        
    def test_edit_device_with_nickname(self, mock_get, mock_post):
        pb = pushbullet.Pushbullet("API_KEY")
        device = pb.devices[0]
        nickname = "New Test Nickname"
        new_device = pb.edit_device(device, nickname=nickname)
        assert new_device.nickname == nickname
        