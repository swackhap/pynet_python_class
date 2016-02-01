import snmp_helper
import time

IP = '50.76.53.27'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr1 = (IP, 7961)
pynet_rtr2 = (IP, 8061)
# Uptime
sysUptime = '1.3.6.1.2.1.1.3.0'
# Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
# Uptime when running config last saved (note any 'write' constitutes a save)
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
# Uptime when startup config last saved
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

sysUptime_raw = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=sysUptime)
print sysUptime_raw
sysuptime_str = snmp_helper.snmp_extract(sysUptime_raw)
sysuptime_flt = float(sysuptime_str)
type(sysuptime_flt)
print sysuptime_flt

current_time_flt = time.time()
print('current time is')
print(current_time_flt)
type(current_time_flt)
time_last_reboot_flt = current_time_flt - sysuptime_flt
print('time_last_reboot_flt is')
print(time_last_reboot_flt)
print('last rebooted at' + time.ctime(time_last_reboot_flt))
'''
print('The current local time is ')
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))

print('The configuration was last saved at ')
print(time.localtime(output))
'''
