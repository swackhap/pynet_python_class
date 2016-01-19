import yaml
import json

dict = {'ip_addr': '192.168.255.21', 'attribs': range(7)};
list = range(8)
list.append('dog')
list.append('cat')
list.append({})
list[-1]=dict
print list

print 'yaml.dump(list)'
print yaml.dump(list)

print 'yaml.dump(list, default_flow_style=False)'
print yaml.dump(list, default_flow_style=False)

print 'yaml.dump(list, default_flow_style=True)'
print yaml.dump(list, default_flow_style=True)
