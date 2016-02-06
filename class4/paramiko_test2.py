
import paramiko
import time
from getpass import getpass

# Define router objects including all parameters needed to connect
# pynet-rtr2
ip_addr = '50.76.53.27'
username = 'pyclass'
#password = getpass()
password = '88newclass'
port = 8022
command_timeout = 0.5
shell_timeout = 6.0

# Initialize Paramiko SSH client
remote_conn_pre=paramiko.SSHClient()

# Tell Paramiko to trust all SSH keys (note: this leaves us open to MITM attacks)
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Open connection to router
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
remote_conn = remote_conn_pre.invoke_shell()

# Set timeout so our SSH session won't hang waiting for additional data to be returned
remote_conn.settimeout(shell_timeout)

# Change terminal length to disable paging
remote_conn.send("terminal length 0\n") 
time.sleep(command_timeout)

# Send command - don't forget carriage return (\n)
remote_conn.send("show run | inc logging\n") 
time.sleep(command_timeout)

# Send command - don't forget carriage return (\n)
remote_conn.send("config t\n") 
time.sleep(command_timeout)

# Send command - don't forget carriage return (\n)
remote_conn.send("logging buffered 37700\n") 
time.sleep(command_timeout)

# Send command - don't forget carriage return (\n)
remote_conn.send("end\n") 
time.sleep(command_timeout)

# Send command - don't forget carriage return (\n)
remote_conn.send("show run | inc logging\n") 
time.sleep(command_timeout)

# Read all buffer data returned from connection up to 5000 bytes
# insert delay to wait for response?
outp = remote_conn.recv(65535)
print outp

# Send command

