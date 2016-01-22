import mock
import json
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

    def test_new_device_with_nickanme(self):
        nickname = "New Dev Test Device"
        new_device = self.pb.new_device(nickname)
        assert self.mock_post.call_count == 1
        assert new_device.nickname == nickname

    def test_new_device_without_nickanme(self):
        new_device = self.pb.new_device(None)
        assert self.mock_post.call_count == 1
        assert new_device.nickname == ""

    def test_edit_device_without_nickname(self):
        new_device = self.pb.edit_device(self.device)
        assert self.mock_post.call_count == 1
        assert new_device.nickname == self.device.nickname

    def test_edit_device_with_nickname(self):
        nickname = "New Test Nickname"
        new_device = self.pb.edit_device(self.device, nickname=nickname)
        assert self.mock_post.call_count == 1
        assert new_device.nickname == nickname

    def test_edit_device_without_model(self):
        new_device = self.pb.edit_device(self.device)
        assert self.mock_post.call_count == 1
        assert new_device.model == self.device.model

    def test_edit_device_with_model(self):
        model = "New Test Model"
        new_device = self.pb.edit_device(self.device, model=model)
        assert self.mock_post.call_count == 1
        assert new_device.model == model

    def test_edit_device_without_manufacturer(self):
        new_device = self.pb.edit_device(self.device)
        assert self.mock_post.call_count == 1
        assert new_device.model == self.device.model

    def test_edit_device_with_manufacturer(self):
        manufacturer = "New Test manufacturer"
        new_device = self.pb.edit_device(self.device, manufacturer=manufacturer)
        assert self.mock_post.call_count == 1
        assert new_device.manufacturer == manufacturer
