"""Test cases for whois of plugin."""
from errbot.rendering import ansiext

pytest_plugins = ['errbot.backends.test']
extra_plugin_dir = '.'


def _packed_ansi_preprocessor__run(self, lines):
    """Patch for https://github.com/errbotio/errbot/issues/1255"""
    text = "\n".join(lines)
    while 1:
        m = self.FENCED_BLOCK_RE.search(text)
        if m:
            code = self._escape(m.group('code'))
            placeholder = self.markdown.htmlStash.store(code)
            text = '%s\n%s\n%s' % (text[:m.start()],
                                   placeholder,
                                   text[m.end():])
        else:
            break
    return text.split("\n")


def test_ok(testbot, monkeypatch):
    """Test for call exists record."""
    with monkeypatch.context() as m:
        m.setattr(
            ansiext.AnsiPreprocessor,
            'run',
            _packed_ansi_preprocessor__run)
        testbot.push_message('!whois example.com')
        assert 'IANA' in testbot.pop_message()


def test_ng_nomatch(testbot, monkeypatch):
    """Test for call exists record."""
    with monkeypatch.context() as m:
        m.setattr(
            ansiext.AnsiPreprocessor,
            'run',
            _packed_ansi_preprocessor__run)
        testbot.push_message('!whois no-example.com')
        assert 'is not found' in testbot.pop_message()
