>>> import snmp_helper
>>> if True:
...   IP = '50.76.53.27'
...   a_user = 'pysnmp'
...   auth_key = 'galileo1'
...   encrypt_key = 'galileo1'
...   snmp_user = (a_user, auth_key, encrypt_key)
...   pynet_rtr1 = (IP, 7961)
...   pynet_rtr2 = (IP, 8061)
...
>>>
>>> snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid='1.3.6.1.2.1.1.5.0')
>>> snmp_data
[(MibVariable(ObjectName('1.3.6.1.2.1.1.5.0')), DisplayString('pynet-rtr1.twb-tech.com', subtypeSpec=ConstraintsIntersection(ConstraintsIntersection(ConstraintsIntersection(ConstraintsIntersection(), ValueSizeConstraint(0, 65535)), ValueSizeConstraint(0, 255)), ValueSizeConstraint(0, 255))))]
>>> output = snmp_helper.snmp_extract(snmp_data)
>>> output
'pynet-rtr1.twb-tech.com'
>>> snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.2.1.1.5.0')
>>> output = snmp_helper.snmp_extract(snmp_data)
>>> output
'pynet-rtr2.twb-tech.com'
>>> snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.2.1.1.1.0')
>>> output = snmp_helper.snmp_extract(snmp_data)
>>> output
'Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)\r\nTechnical Support: http://www.cisco.com/techsupport\r\nCopyright (c) 1986-2014 by Cisco Systems, Inc.\r\nCompiled Thu 26-Jun-14 14:15 by prod_rel_team'
>>> print output
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Thu 26-Jun-14 14:15 by prod_rel_team
>>>


# Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'

# Uptime when running config last saved (note any 'write' constitutes a save)
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'

# Uptime when startup config last saved
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

