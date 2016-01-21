import yaml

#Get base filename input from user for file to be read
filename_base = raw_input("What is the base yaml filename to be read? :")

#Open file and read into variable "list"
with open(filename_base + ".yml") as f:
    list = yaml.load(f)

#Pretty-print
print 'yaml.dump(list,default_flow_style=False)'
print yaml.dump(list,default_flow_style=False)
