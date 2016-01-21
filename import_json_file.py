import json 

#Get base filename input from user for file to be read
filename_base = raw_input("What is the base json filename to be read? :")

#Open file and read into variable "list"
print 'Opening JSON file for reading'
with open(filename_base + ".json") as f:
    list = json.load(f)

#Pretty-print
print 'json.dumps(list)'
print json.dumps(list)
