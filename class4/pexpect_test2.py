
import pexpect
import sys
from getpass import getpass

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    #password = getpass()
    password = '88newclass'

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')

    ssh_conn.sendline('show run | inc logging')
    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('config t')
    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('logging buffered 37789')
    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('end')
    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after

    ssh_conn.sendline('show run | inc logging')
    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after

if __name__ == "__main__":
    main()
