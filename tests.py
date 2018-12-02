"""Test cases of plugin."""
pytest_plugins = ['errbot.backends.test']
extra_plugin_dir = '.'


def test_ok__no_type_specific(testbot):
    """Test for call only FQDN(not specify record type)."""
    testbot.push_message('!dig example.com')
    assert 'A records of example.com' in testbot.pop_message()


def test_ok__with_specify_type(testbot):
    """Test for call FQDN with type."""
    testbot.push_message('!dig -t NS example.com')
    assert 'NS records of example.com' in testbot.pop_message()


def test_ng__no_record(testbot):
    """No answered query."""
    testbot.push_message('!dig norec.example.com')
    reply = testbot.pop_message()
    assert 'A records of norec.example.com' in reply
    assert 'is not found.' in reply
