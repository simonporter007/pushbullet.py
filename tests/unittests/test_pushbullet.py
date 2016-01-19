import mock
from pushbullet import pushbullet
from mock_response import mocked_requests_get, mocked_requests_post, mocked_requests_delete

class TestPushbullet(object):
    
    def setup_method(self, method):
        self.patchers = []
        patcher_get = mock.patch('pushbullet.pushbullet.requests.Session.get', side_effect=mocked_requests_get)
        patcher_post = mock.patch('pushbullet.pushbullet.requests.Session.post', side_effect=mocked_requests_post)
        patcher_delete = mock.patch('pushbullet.pushbullet.requests.Session.delete', side_effect=mocked_requests_delete)
        self.patchers.extend([patcher_get, patcher_post, patcher_delete])
        self.mock_get = patcher_get.start()
        self.mock_post = patcher_post.start()
        self.mocked_requests_delete = patcher_delete.start()
        self.pb = pushbullet.Pushbullet("API_KEY")
        self.device = self.pb.devices[0]
    
    def teardown_method(self, method):
        for patcher in self.patchers:
            patcher.stop()
        
    def test_edit_device_without_nickname(self):
        new_device = self.pb.edit_device(self.device)
        assert new_device.nickname == self.device.nickname
        
    def test_edit_device_with_nickname(self):
        nickname = "New Test Nickname"
        new_device = self.pb.edit_device(self.device, nickname=nickname)
        assert new_device.nickname == nickname
        
