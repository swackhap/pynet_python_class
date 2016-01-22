from ciscoconfparse import CiscoConfParse

# Read file for parsing into variable "file"
filename = 'cisco_ipsec.txt'
print 'Opening ' + filename + ' file for reading'
file = open(filename, 'r')
print file.read()

# Parse file into variable "cisco_cfg"
print 'Output of cisco_cfg = CiscoConfParse(' + filename + ') is:'
cisco_cfg = CiscoConfParse(filename)
print cisco_cfg

# Find all 'crypto map CRYPTO' lines and print them with their children
crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")
 
print "crypto_maps are:"
for i in crypto_maps:
  print i.text

crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'^crypto map CRYPTO', childspec=r'pfs group2')

print "crypto_maps configs are:"
i = 0
for count in crypto_maps:
  print crypto_maps[i].text
  for child in crypto_maps[i].all_children:
    print child.text
  i = i + 1


# Find all crypto map entries using PFS group2

# Find all crypto map entries not using AES (based on the transform set name)



