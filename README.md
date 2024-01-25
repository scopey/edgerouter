# Edgerouter scripts for the ER-X, ER-4, and likely other non UDM devices
Edgerouter scripts I use

lease.py 

Grabs the current DHCP leases from the EdgeRouter and puts them into JSON.  You can do whatever you like from there.
To use the script as is you need to set ENV variables for USER, PASS and HOST.  This is less secure than lease-sshkey.py 

lease-sshkey.py

Does the same as lease.py but more securely.  You need to have a ssh key setup with the router and make sure the entry is in the known_hosts file.  

