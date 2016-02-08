
from netmiko import ConnectHandler
from getpass import getpass

def main():
    #password = getpass()
    password = '88newclass'

    # Define libraries for devices we will connect to
    pynet1 = {
        'device_type': 'cisco_ios',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': password,
        'port': 22,
    }
    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': password,
        'port': 8022,
    }
    juniper_srx = {
        'device_type': 'juniper',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': password,
        'port': 9822,
    }



    rtr1 = ConnectHandler(**pynet1)
    rtr2 = ConnectHandler(**pynet2)
    srx = ConnectHandler(**juniper_srx)
    
    outp = rtr1.send_command("show arp") 
    print "rtr1 show arp:"
    print outp
    outp = rtr2.send_command("show arp") 
    print "rtr2 show arp:"
    print outp
    outp = srx.send_command("show arp") 
    print "srx show arp:"
    print outp

if __name__ == "__main__":
    main()
