"""Test cases for whois of plugin."""
pytest_plugins = ['errbot.backends.test']
extra_plugin_dir = '.'


def test_ok(testbot):
    """Test for call exists record."""
    testbot.push_message('!whois example.com')
    assert 'IANA' in testbot.pop_message()
