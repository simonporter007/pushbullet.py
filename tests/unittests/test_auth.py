import pytest
import mock
import pushbullet

@mock.patch('pushbullet.Pushbullet._get_data')
class TestAuth(object):

    def test_auth_fail(self, mock__get_data):
        mock__get_data.side_effect = pushbullet.errors.InvalidKeyError()
        with pytest.raises(pushbullet.InvalidKeyError) as exinfo:
            pb = pushbullet.Pushbullet("faultykey")

    def test_auth_success(self, mock__get_data):
        mock__get_data.return_value = { "name" : "Pushbullet Tester" }
        pb = pushbullet.Pushbullet("validKey")
        assert pb.user_info["name"] == "Pushbullet Tester"