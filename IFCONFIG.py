import ifcfg
import json

for name, interface in ifcfg.interfaces().items():
    # do something with interface
    print (interface['device'])       # Device name
    print (interface['inet'])         # First IPv4 found
    print (interface['inet4'])        # List of ips
    print (interface['inet6'])       # List of ips
    print (interface['netmask'])      # Backwards compat: First netmask
    print (interface['netmasks'])     # List of netmasks
    print (interface['broadcast'])    # Backwards compat: First broadcast
    print (interface['broadcasts'])   # List of broadcast

# print(ifcfg.default_interface()) # Ignore this line still working on this line, trying to find source of execution error.