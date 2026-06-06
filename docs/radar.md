# Radar DNS

`radar.birki.io` points directly at the Radar service's Tailscale IPv4 address.
It is intentionally unproxied because Cloudflare cannot proxy traffic to
Tailscale-only addresses.

This record is a temporary stable service name while the native MagicDNS
hostname is not reliable on every client. Revisit this workaround when MagicDNS
for the endpoint resolves through both the system resolver and direct Quad100
queries again.
