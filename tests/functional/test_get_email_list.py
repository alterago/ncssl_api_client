import unittest
import mock
import sys
from ncssl_api_client.__main__ import main


@mock.patch('ncssl_api_client.api.api_client.ApiClient.send_call', return_value='test api response')
@mock.patch('ncssl_api_client.config.manager.ConfigManager.get_api_command_config')
@mock.patch('ncssl_api_client.config.manager.ConfigManager.get_api_sandbox_client_config')
class GetEmailListTest(unittest.TestCase):

    def test_success_flow(self, api_config_mock, command_config_mock, api_client_mock):
        with mock.patch('sys.argv', ['ncsslapi', 'get_email_list', '-t', 'PositiveSSL', '-d', 'example.com', '-sb']):
            self.assertEqual(main(), 'test api response')

