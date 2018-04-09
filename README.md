# enpm685
ENPM685 class examples

* wget.py - Roll your own wget in Python (usage wget.py http://url.to.get file-to-save-as)
* httpbanner.py - Grab HTTP Server banner information (usage httpbanner.py http://url)

**Wordpress Checking examples**

Usage wordpress-check.py http://url.to.check (use http://msmc.umd.edu for an example)

* wordpress-check.py - Initial take at a script to check to see if a site is a Wordpress site
* wordpress-check2.py - Making it more flexible
* wordpress-check3.py - Adding something to grab robots.txt

**Tor Exit Node examples** 

* exit_node.py - Initial Tor Exit Node grabber - Usage exit_node.py
* exit_node2.py - Save Tor Exit Node list to "tor_exit_nodes.txt" - Usage exit_node2.py
* exit_node3.py - Customize with saving a file name - Usage exit_note3.py filename
* exit_node4.py - Introduce different formats - Usage exit_node4.py -f format filename (where format = csv, palo, cidr)
* exit_node5.py - Add iptables - Usage exit_node4.py -f format filename (where format = csv, palo, cidr, iptables)
