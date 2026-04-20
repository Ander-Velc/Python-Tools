#!/usr/bin/env python3

from scapy.all import TCP, IP, sr1, send
import random
import signal
import argparse
import time

# --------------------------------
# CTRL + C Function
# --------------------------------
def def_handler(sig, frame):
    print("\nCTRL + C --> Exit...")
    exit(0)

signal.signal(signal.SIGINT, def_handler)

# --------------------------------
# Starting and Ending Scan Banner
# --------------------------------
def scanBanner(ip):
    date = time.strftime("%Y-%m-%d %H:%M:%S") 
    print(f"Starting scan... (https://github.com/ander-velc) at {date}")
    print(f"Scan report for {ip}\n")
def end_scanBanner():
    date = time.strftime("%Y-%m-%d %H:%M:%S") 
    print(f"\nScan done at {date}")

# -------------------------
# Port Services
# -------------------------
def get_service(port):
    services = {
        1: "tcpmux",
        5: "rje",
        7: "echo",
        9: "discard",
        11: "systat",
        13: "daytime",
        17: "qotd",
        18: "msp",
        19: "chargen",
        20: "ftp-data",
        21: "ftp",
        22: "ssh",
        23: "telnet",
        25: "smtp",
        37: "time",
        42: "nameserver",
        43: "whois",
        49: "tacacs",
        50: "re-mail-ck",
        53: "dns",
        67: "dhcp-server",
        68: "dhcp-client",
        69: "tftp",
        70: "gopher",
        79: "finger",
        80: "http",
        88: "kerberos",
        101: "hostname",
        102: "iso-tsap",
        107: "rtelnet",
        109: "pop2",
        110: "pop3",
        111: "rpcbind",
        113: "ident",
        119: "nntp",
        123: "ntp",
        137: "netbios-ns",
        138: "netbios-dgm",
        139: "netbios-ssn",
        143: "imap",
        161: "snmp",
        162: "snmptrap",
        177: "xdmcp",
        179: "bgp",
        194: "irc",
        199: "smux",
        201: "apple-talk",
        209: "qmtp",
        210: "z39.50",
        213: "ipx",
        218: "mpp",
        220: "imap3",
        389: "ldap",
        443: "https",
        445: "microsoft-ds",
        464: "kpasswd",
        465: "smtps",
        500: "isakmp",
        512: "exec",
        513: "login",
        514: "shell",
        515: "printer",
        520: "rip",
        521: "ripng",
        540: "uucp",
        543: "klogin",
        544: "kshell",
        546: "dhcpv6-client",
        547: "dhcpv6-server",
        548: "afp",
        554: "rtsp",
        563: "nntps",
        587: "submission",
        591: "filemaker",
        593: "http-rpc-epmap",
        636: "ldaps",
        639: "msdp",
        646: "ldp",
        666: "doom",
        674: "acap",
        691: "msexch-routing",
        860: "iscsi",
        873: "rsync",
        902: "vmware-auth",
        989: "ftps-data",
        990: "ftps",
        993: "imaps",
        995: "pop3s",
        1025: "nfs-or-iis",
        1080: "socks",
        1194: "openvpn",
        1214: "kazaa",
        1241: "nessus",
        1311: "rxmon",
        1337: "backdoor",
        1433: "mssql",
        1434: "mssql-monitor",
        1521: "oracle",
        1701: "l2tp",
        1723: "pptp",
        1755: "ms-streaming",
        1812: "radius",
        1813: "radius-acct",
        1863: "msn",
        1900: "upnp",
        1935: "rtmp",
        2000: "cisco-sccp",
        2049: "nfs",
        2082: "cpanel",
        2083: "cpanel-ssl",
        2086: "whm",
        2087: "whm-ssl",
        2095: "webmail",
        2096: "webmail-ssl",
        2100: "amiganetfs",
        2222: "directadmin",
        2375: "docker",
        2376: "docker-ssl",
        2483: "oracle-ssl",
        2484: "oracle-ssl-alt",
        2485: "oracle",
        3000: "node",
        3001: "node-alt",
        3128: "squid-proxy",
        3260: "iscsi-target",
        3306: "mysql",
        3389: "rdp",
        3690: "subversion",
        4000: "icq",
        4040: "spark",
        4444: "metasploit",
        4500: "ipsec-nat-t",
        4567: "tram",
        4662: "edonkey",
        4899: "radmin",
        5000: "upnp-alt",
        5001: "commplex-link",
        5060: "sip",
        5061: "sips",
        5432: "postgresql",
        5500: "vnc",
        5601: "kibana",
        5631: "pcanywhere",
        5666: "nrpe",
        5800: "vnc-http",
        5900: "vnc",
        5985: "winrm",
        5986: "winrm-ssl",
        6000: "x11",
        6379: "redis",
        6443: "kubernetes",
        6667: "irc",
        7001: "weblogic",
        7002: "weblogic-ssl",
        7077: "spark",
        7199: "cassandra",
        7200: "fodms",
        7474: "neo4j",
        7601: "splunk",
        7777: "game",
        8000: "http-alt",
        8008: "http-alt",
        8080: "http-proxy",
        8081: "http-alt",
        8086: "influxdb",
        8087: "simplifymedia",
        8088: "radan-http",
        8090: "opsmessaging",
        8091: "couchbase",
        8100: "xprint-server",
        8181: "http-alt",
        8222: "vmware",
        8333: "bitcoin",
        8443: "https-alt",
        8500: "consul",
        8600: "consul-dns",
        8765: "ultraseek",
        8888: "http-alt",
        9000: "sonarqube",
        9042: "cassandra",
        9092: "kafka",
        9093: "kafka-ssl",
        9100: "printer",
        9200: "elasticsearch",
        9418: "git",
        9443: "https-alt",
        9500: "ismserver",
        9999: "abyss",
        10000: "webmin",
        11211: "memcached",
        27017: "mongodb"
    }
    return services.get(port, "")

# -------------------------
# Scanner Stealth Scan
# -------------------------
def sS_scanner(ip, port): 
    sport = random.randint(1024, 65535)
    packet = IP(dst=ip)/TCP(sport=sport, dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)

    if response is None:
        return "FILTERED"

    if response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            send(IP(dst=ip)/TCP(sport=sport, dport=port, flags="R"), verbose=0)
            return "OPEN"
        elif response[TCP].flags == 0x14:
            return "CLOSED"

    return "UNKNOWN"

# -------------------------
# Only Open Ports
# -------------------------
def sS_scanner_openPorts(ip, port): 
    sport = random.randint(1024, 65535)
    packet = IP(dst=ip)/TCP(sport=sport, dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)

    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            send(IP(dst=ip)/TCP(sport=sport, dport=port, flags="R"), verbose=0)
            return True
    return False

# -------------------------
# MAIN
# -------------------------
def main(): 

    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("-i", "--ip", required=True, help="Target IP")
    parser.add_argument("-p", "--ports", help="Range ex: 20-100")
    parser.add_argument("--open", action="store_true", help="Show only open ports")
    parser.add_argument("-p-", "--all-ports", action="store_true", help="Scan 1-65535") 
    args = parser.parse_args()

    ip = args.ip 
    scanBanner(ip)

    if args.all_ports:
        ports = range(1, 65536)
    elif args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)
    else:
        print("You must specify -p <ports> or -p- <all-ports>")
        return
    print(f"{'PORT':<10}{'STATE':<10}{'SERVICE':<15}")
    for port in ports:
        service = get_service(port)
        port_str = f"{port}/tcp"
        if args.open:
            if sS_scanner_openPorts(ip, port):
                print(f"{port_str:<10}{'open':<10}{service:<15}")
        else:
            state = sS_scanner(ip, port).lower()
            print(f"{port_str:<10}{state:<10}{service:<15}") 

    end_scanBanner()

if __name__ == "__main__":
    sdate = time.perf_counter()
    main()
    fdate = time.perf_counter()
    print(f"Host was scanned in {fdate - sdate:.6f} seconds")
