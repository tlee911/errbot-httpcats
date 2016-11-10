import os
import httpcats
from errbot.backends.test import testbot


class TestRemoteBot(object):
    extra_plugin_dir = '.'

    def test_http(self, testbot):
        testbot.push_message('!http')
        assert 'Usage' in testbot.pop_message()

    def test_http_valid(self, testbot):
        testbot.push_message('!http 400')
        assert 'https://http.cat/400' in testbot.pop_message()

    def test_http_invalid(self, testbot):
        for code in ['555', 'abc', '1']:
            testbot.push_message('!http {0}'.format(code))
            assert 'Not a valid HTTP status code' in testbot.pop_message()

    def test_http_regex(self, testbot):
        for message in ['http200', 'http 200', 'http  2001']:
            testbot.push_message(message)
            assert 'https://http.cat/200' in testbot.pop_message()