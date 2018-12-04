"""Errbot netutils plugin."""
import textwrap

import dns.resolver
import whois
from errbot import BotPlugin, arg_botcmd

DNS_RECORD_TYPES = [
    'A',
    'AAAA',
    'CNAME',
    'MX',
    'NS',
    'SOA',
    'TXT',
]

DNS_RECORD_TYPE_CHOICES = DNS_RECORD_TYPES \
    + [t.lower() for t in DNS_RECORD_TYPES]


class NetUtils(BotPlugin):
    """Net util commands."""

    @arg_botcmd('fqdn', type=str)
    @arg_botcmd(
        '-t', dest='record_type', type=str,
        choices=DNS_RECORD_TYPE_CHOICES, default='A')
    def dig(self, message, fqdn, record_type):
        """Look up DNS record."""
        try:
            answers = dns.resolver.query(fqdn, record_type)
            return f'**{record_type.upper()} records of {fqdn}**\n\n' \
                + '\n'.join([f'* `{r.to_text()}`' for r in answers])
        except dns.resolver.NXDOMAIN:
            return f'**{record_type.upper()} records of {fqdn}** is not found.'

    @arg_botcmd('domain', type=str)
    def whois(self, message, domain):
        """Fetch WHOIS information."""
        try:
            result = whois.whois(domain)
            msg = f'''
                **WHOIS information of {domain}**
                \`\`\`
                {result.text}
                \`\`\`
                '''  # noqa: W605
            return textwrap.dedent(msg).strip()
        except whois.parser.PywhoisError:
            return f'WHOIS information of **{domain}** is not found.'
