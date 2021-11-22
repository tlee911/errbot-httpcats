from errbot.backends.test import testbot
from unittest.mock import MagicMock
import httpcats
import os


class TestRemoteBot(object):
    extra_plugin_dir = '.'

    def test_http(self, testbot):
        testbot.push_message('!http')
        assert 'Usage' in testbot.pop_message()

    def test_http_valid(self, testbot):
        helper_mock = MagicMock(return_value=True)
        testbot.inject_mocks('HttpCats', {'has_cat': helper_mock})

        testbot.push_message('!http 400')
        assert 'https://http.cat/400' in testbot.pop_message()

    def test_http_invalid(self, testbot):
        helper_mock = MagicMock(return_value=False)
        testbot.inject_mocks('HttpCats', {'has_cat': helper_mock})

        for code in ['555', 'abc', '1']:
            testbot.push_message('!http {0}'.format(code))
            assert 'Not a valid HTTP status code' in testbot.pop_message()

    def test_http_regex(self, testbot):
        helper_mock = MagicMock(return_value=True)
        testbot.inject_mocks('HttpCats', {'has_cat': helper_mock})

        for message in ['http200', 'http 200', 'http  2001']:
            testbot.push_message(message)
            assert 'https://http.cat/200' in testbot.pop_message()
