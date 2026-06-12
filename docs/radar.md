# Radar DNS

`radar-core.birki.io` and `radar.birki.io` point directly at the Radar host's Tailscale IPv4 address. They are intentionally unproxied because Cloudflare cannot proxy traffic to Tailscale-only addresses.

- `radar-core.birki.io`: operational Radar endpoint for OpenObserve, API access, and Vector ingest.
- `radar.birki.io`: authenticated read-only Radar dashboard.

These records are stable service names while native MagicDNS is not reliable on every client. Revisit this workaround when MagicDNS resolves through both the system resolver and direct Quad100 queries again.
