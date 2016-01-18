import mock
from pushbullet import pushbullet
from mock_response import mocked_requests_get, mocked_requests_post

class TestPushbullet(object):
    
    def setup_method(self, method):
        self.patcher_get = mock.patch('pushbullet.pushbullet.requests.Session.get', side_effect=mocked_requests_get)
        self.patcher_post = mock.patch('pushbullet.pushbullet.requests.Session.post', side_effect=mocked_requests_post)
        self.mock_get = self.patcher_get.start()
        self.mock_post = self.patcher_post.start()
        self.pb = pushbullet.Pushbullet("API_KEY")
        self.device = self.pb.devices[0]
    
    def teardown_method(self, method):
        self.patcher_get.stop()
        self.patcher_post.stop()
        
    def test_edit_device_without_nickname(self):
        new_device = self.pb.edit_device(self.device)
        assert new_device.nickname == self.device.nickname
        
    def test_edit_device_with_nickname(self):
        nickname = "New Test Nickname"
        new_device = self.pb.edit_device(self.device, nickname=nickname)
        assert new_device.nickname == nickname
        
    def test_edit_device_without_model(self):
        new_device = self.pb.edit_device(self.device)
        assert new_device.model == self.device.model
        
    def test_edit_device_with_model(self):
        model = "New Test Model"
        new_device = self.pb.edit_device(self.device, model=model)
        assert new_device.model == model
        
    def test_edit_device_without_manufacturer(self):
        new_device = self.pb.edit_device(self.device)
        assert new_device.model == self.device.model
        
    def test_edit_device_with_manufacturer(self):
        manufacturer = "New Test manufacturer"
        new_device = self.pb.edit_device(self.device, manufacturer=manufacturer)
        assert new_device.manufacturer == manufacturer
        