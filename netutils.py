"""Errbot netutils plugin."""
import dns.resolver
from errbot import BotPlugin, arg_botcmd


class Netutils(BotPlugin):
    """Net util commands."""

    @arg_botcmd('fqdn', type=str)
    def dig(self, message, fqdn):
        """Look up DNS record."""
        answers = dns.resolver.query(fqdn, 'A')
        return f'**Answes for {fqdn}**\n\n' \
            + '\n'.join([f'* {r.address}' for r in answers])
