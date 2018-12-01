"""Errbot netutils plugin."""
import dns.resolver
from errbot import BotPlugin, arg_botcmd

DNS_RECORD_TYPES = [
    'A',
    # TODO: Implement after
    # 'AAAA',
    # 'CNAME',
    # 'MX',
    # 'SOA',
    # 'TXT',
]

DNS_RECORD_TYPE_CHOICES = DNS_RECORD_TYPES \
    + [t.lower() for t in DNS_RECORD_TYPES]


class Netutils(BotPlugin):
    """Net util commands."""

    @arg_botcmd('fqdn', type=str)
    @arg_botcmd(
        '-t', dest='record_type', type=str,
        choices=DNS_RECORD_TYPE_CHOICES, default='A')
    def dig(self, message, fqdn, record_type):
        """Look up DNS record."""
        answers = dns.resolver.query(fqdn, record_type)
        return f'**Answers for {fqdn}**\n\n' \
            + '\n'.join([f'* {r.address}' for r in answers])
