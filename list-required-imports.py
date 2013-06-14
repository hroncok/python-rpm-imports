import re

f = open('input.txt','r')
text = f.read()
f.close()

modules = set()

# import foo, bar
match = re.findall( r'^(?: *|\t*)import[ |\t]+([\w|-|,| |\t]*)$', text, re.M|re.I)
for line in match:
   line = line.split(',')
   modules.update([x.strip() for x in line])

# from foo import bar
match = re.findall( r'^(?: *|\t*)from[ |\t]+(\w|-)+[ |\t]+import\s+([\w|-|,| |\t]*)$', text, re.M|re.I)
for line in match:
   line = line[0], line[1].split(',')
   modules.update([line[0].strip()+'.'+x.strip() for x in line[1]])

# from foo import *
match = re.findall( r'^(?: *|\t*)from[ |\t]+(\w|-)+[ |\t]+import\s+\*$', text, re.M|re.I)
modules.update(match)
   
for module in modules:
   print(module)
