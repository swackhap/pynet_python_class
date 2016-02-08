
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
    srx = {
        'device_type': 'juniper',
        'ip': '50.76.53.27',
        'username': 'pyclass',
        'password': password,
        'port': 9822,
    }


    pynet_rtr2 = ConnectHandler(**pynet2)
    pynet_rtr2.config_mode()
    outp = pynet_rtr2.find_prompt()
    print outp
    outp2 = pynet_rtr2.check_config_mode()
    print 'Config mode status is ' + str(outp2)
    

if __name__ == "__main__":
    main()
