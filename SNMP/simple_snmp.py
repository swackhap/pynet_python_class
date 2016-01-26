
from snmp_helper import snmp_get_oid,snmp_extract

#pynet-rtr1 = 50.76.53.27:7961
COMMUNITY_STRING = 'galileo'
SNMP_PORT = 7961
IP = '50.76.53.27'
OID_LIST = ('1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.5.0')

a_device = (IP, COMMUNITY_STRING, SNMP_PORT)
print '-->Connecting to pynet-rtr1 at IP ' + a_device[0] + \
    ' port ' + str(a_device[2]) + ' with community string ' + a_device[1] 
for oid in OID_LIST:
    snmp_data = snmp_get_oid(a_device, oid=oid)
    output = snmp_extract(snmp_data)
    print '\n OID ' + oid + ' value is \n' + output + '\n'

#pynet-rtr2 = 50.76.53.27:8061
COMMUNITY_STRING = 'galileo'
SNMP_PORT = 8061
IP = '50.76.53.27'
OID_LIST = ('1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.5.0')

a_device = (IP, COMMUNITY_STRING, SNMP_PORT)
print '-->Connecting to pynet-rtr2 at IP ' + a_device[0] + \
    ' port ' + str(a_device[2]) + ' with community string ' + a_device[1] 
for oid in OID_LIST:
    snmp_data = snmp_get_oid(a_device, oid=oid)
    output = snmp_extract(snmp_data)
    print '\n OID ' + oid + ' value is \n' + output + '\n'
