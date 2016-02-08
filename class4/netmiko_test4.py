
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



#    rtr1 = ConnectHandler(**pynet1)
#    rtr2 = ConnectHandler(**pynet2)
#    srx = ConnectHandler(**juniper_srx)
    
    all_devices = [pynet1, pynet2]

    for a_device in all_devices:
        net_connect = ConnectHandler(**a_device)
        outp = net_connect.send_command("show run | inc logging")
        print outp
        outp = net_connect.send_config_from_file(config_file='config_file.txt')
        print outp
        outp = net_connect.send_command("show run | inc logging")
        print outp

if __name__ == "__main__":
    main()
