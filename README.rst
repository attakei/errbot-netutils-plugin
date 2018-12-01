errbot-netutils
===============

Network util tools for Errbot (dig)

Overview
--------

This is Errbot plugin that can fetch network information.

Currently, this can fetch these data.

* DNS record

Why make it?
------------


Recently engineers use docker as application hosting.
Especially, Alpine Linux is used often because is lightweight for base image.

But, becuase Alpine does not have dig command, need install "dig" manually to use dnsutils.

This plugin has goal to serve network information independ on OS systems.

