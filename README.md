# I have to write a readme bruh
Basically this script is just four basic steps, put into a python script because i got sick of using the interactive CLI to do this.
You still need a giant .pcap for it to work. i usually use wireshark because you can be sure it's not just hung.

1 - Scan all frames, discard non-ether frames(if you have a lot you might be in monitor mode. dont do that)
2 - look for MAC addresses. Either source or destination works, but just find every MAC in the pcap. Hopefully this includes mDNS from other passengers who ARE paying for internet
3 - overwrite your network card's MAC address with each MAC the script now knows, and if you type "yes", it'll terminate, else, try the next oe.
That's intended to give NetworkManager time to reconnect, and for you to, say,``ping 1.1.1.1``, to check if the MAC address is invalid or works.
This is very much NOT an easy tool to use, if you somehow found my goofy ahh code pls just write ur own, mine is insanely fragile.
It assumes:
- You have scapy installed
- You have a proper non-corrupt .pcap that scapy can parse
- Subprocess.run works in your python version
- you use python3
- running with shell=True works(you have a working sh)
- sudo exists(no doas), and you get the password right
- ifconfig exists
- you know basic networking

  If it tells you to whip out monitor mode & nukes, don't actually feed it a monitor mode pcap, that's just a joke(and failure message) lol
