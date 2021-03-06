import yaml
import json

#Get base filename input from user for yaml and json files to be created
filename_base = raw_input("What will the base filename be for yaml and json files? :")

dict = {'ip_addr': '192.168.255.21', 'attribs': range(7)};
list = range(8)
list.append('dog')
list.append('cat')
list.append({})
list[-1]=dict

#Print list in raw python form
print list

#Print list in raw yaml form
print 'yaml.dump(list)'
print yaml.dump(list)

#Print list in yaml form with default flow style off--more human readable
print 'yaml.dump(list, default_flow_style=False)'
print yaml.dump(list, default_flow_style=False)

#Print list in yaml form with default flow style on
print 'yaml.dump(list, default_flow_style=True)'
print yaml.dump(list, default_flow_style=True)

#Print list in json form
print 'json.dumps(list)'
print json.dumps(list)

#Write list to yaml file in long form
#yaml filename
yaml_filename = filename_base + '.yml'
print 'Writing yaml file ' + filename_base + '.yml'
with open(yaml_filename, "w") as f:
    f.write(yaml.dump(list, default_flow_style=False))

#json filename
json_filename = filename_base + '.json'
print 'Writing json file ' + json_filename
with open(json_filename, "w") as f:
    json.dump(list,f)
