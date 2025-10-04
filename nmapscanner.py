##Create a Python tool that can scan a network for open ports, services, and vulnerabilities. Libraries like Scapy or Nmap can be helpful.##

import nmap


def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sS -sV -O')
    return nm.all_hosts()

if __name__ == "__main__":
    target = input("Enter the target IP: ")
    hosts = scan_network(target)
    print("Scan complete. Hosts found:")
    for host in hosts:
        print(f" - {host}")