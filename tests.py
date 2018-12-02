"""Test cases of plugin."""
pytest_plugins = ['errbot.backends.test']
extra_plugin_dir = '.'


def test_ok__no_type_specific(testbot):
    """Test for call only FQDN(not specify record type)."""
    testbot.push_message('!dig example.com')
    assert 'A records of example.com' in testbot.pop_message()
