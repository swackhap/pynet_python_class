import snmp_helper
import time
import pickle

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

# Get sysUptime

# Initialize pickle file if it doesn't currently exist
# touch filename.pkl
# put in 2440 for first number since that's the value it would be at startup time
'''
f = open("config_change_uptime_samples.pkl", "wb")
init_data = ['2440','3000']
pickle.dump(init_data, f)
f.close()
'''

# Get system uptime when config last changed
time_config_last_changed_raw = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, 
                             oid=ccmHistoryRunningLastChanged)
time_config_last_changed_str = snmp_helper.snmp_extract(time_config_last_changed_raw)

# Open pickle file and read in all prior data samples
f = open("config_change_uptime_samples.pkl", "rb")
config_change = pickle.load(f)
print "config_change loaded from pickle file:"
print config_change
f.close()

# Append the last config change system time to local data structure
config_change.append(time_config_last_changed_str)
print "config_change appended with most recent data:"
print config_change

# Append the last config change system time to a data structure
f = open("config_change_uptime_samples.pkl", "wb")
pickle.dump(config_change, f)
f.close()

# Check if config changed since last run
delta_time = float(config_change[-1]) - float(config_change[-2])
if delta_time > 0:
  print "\nConfig has changed since last check"
elif delta_time < 0:
  print "\nRouter rebooted or data is corrupt"
else:
  print "\nNo config change since last check"

'''
current_time_flt = time.time()
print('\ncurrent time as flt is')
print(current_time_flt)
print('\nCurrent time is ' + time.ctime(current_time_flt))

sysUptime_raw = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=sysUptime)
sysuptime_str = snmp_helper.snmp_extract(sysUptime_raw)
sysuptime_flt = float(sysuptime_str)
print('\nsysuptime_flt is ')
print(sysuptime_flt)

time_last_reboot_flt = current_time_flt - sysuptime_flt
print('\ntime_last_reboot_flt is')
print(time_last_reboot_flt)
print('\nlast rebooted at ' + time.ctime(time_last_reboot_flt))

time_config_last_changed_raw = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, 
                             oid=ccmHistoryRunningLastChanged)
print(time_config_last_changed_raw)
time_config_last_changed_str = snmp_helper.snmp_extract(time_config_last_changed_raw)
time_config_last_changed_flt = float(time_config_last_changed_str)
print('\ntime_config_last_changed_flt is ')
print(time_config_last_changed_flt)

print('\nRunning config last changed at ' + time.ctime(time_config_last_changed_flt))
'''
