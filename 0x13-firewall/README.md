# 0x13. Firewall

Firewalls are network security devices that are used to monitor and
control incoming and outgoing network traffic based on a set of
predefined security rules. Their primary goal is to protect a network
from unauthorized access, attacks, and other malicious activities.

Firewalls can be implemented as hardware, software, or a combination of
both. They are placed at strategic points within a network, typically at
the network perimeter, to create a barrier between trusted and untrusted
networks.

Firewalls work by examining each packet of network traffic that passes
through them and comparing it against a set of rules or policies. If a
packet matches a rule, it is either allowed to pass through the firewall
or blocked, depending on the rule's configuration.

UFW, or Uncomplicated Firewall, is a simplified firewall management
interface that hides the complexity of lower-level packet filtering
technologies such as `iptables` and `nftables`.
