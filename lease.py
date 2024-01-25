import paramiko
import re
import json
import os

# Get the user name and password from the ENV variables
# You should use USER and PASS and HOST as the env variables 
# You can also change the ssh.connect line to the actual values but this is not recommended

USER = os.environ.get("USER")
PASS = os.environ.get("PASS")
HOST = os.environ.get("HOST")

# Connect to the EdgeRouter via SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=HOST, username=USER, password=PASS)

# Execute the SSH command to retrieve DHCP leases
stdin, stdout, stderr = ssh.exec_command("/usr/sbin/ubnt-dhcp print-leases")

output = stdout.read().decode()

# Parse the output into a list of dictionaries
leases = []
for line in output.splitlines()[2:]:  # Skip header lines
    fields = line.strip().split(maxsplit=5)  # Split into at most 5 fields
    if len(fields) < 6:
        fields.append("none")  # Add "none" for missing fields
    
    lease_data = {
        "IP address": fields[0],
        "Hardware Address": fields[1],
        "Lease expiration": fields[2] + " " + fields[3],  # Combine date and time
        "Pool": fields[4],
        "Client Name": fields[5],
    }
    leases.append(lease_data)

# Convert the list of dictionaries to JSON
json_data = json.dumps(leases, indent=4)

print(json_data)

# Close the SSH connection
ssh.close()
