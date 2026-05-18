# n_mapper

A TCP and UDP network scanner built with Python that identifies open ports on a target IP using protocol-specific payloads for accurate UDP detection.

## How it works

- TCP scanning uses a full connection attempt (SYN, SYN-ACK, ACK) to determine if a port is open
- UDP scanning sends protocol-specific payloads to 50 well-known ports, derived from Nmap's service probes, to elicit real responses rather than relying on ICMP unreachable messages
- Ports with no specific payload fall back to an empty probe and are marked `open or filtered` if no response is received

## Requirements

- Python 3
- `udpayloads.py` must be in the same directory as `map.py`

## Usage

```bash
python3 map.py
```

You will be prompted to enter:
- Target IP address
- Protocol (TCP, UDP, or both)
- Port range (`x-y`) or specific ports (`x,y,z`)

## UDP payload coverage

Protocol-specific payloads are included for 50 ports including DNS (53), NTP (123), SNMP (161), DHCP (67), SIP (5060), Kerberos (88), LDAP (389), NetBIOS (137), RIP (520), L2TP (1701), MSSQL (1433), NFS (2049), and more.

## Disclaimer

This tool is intended for educational purposes and use in controlled lab environments only. Only use against systems you own or have explicit permission to scan. Unauthorized port scanning may be illegal in your jurisdiction.
