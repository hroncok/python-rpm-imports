import re, os, sys

modules = set()

for root, subs, files in os.walk(sys.argv[1]):
   for file in files:
      try:
         with open(os.path.join(root,file)) as f:
            text = f.read()
      except:
         pass
      
      # import foo, bar
      match = re.findall( r'^(?: *|\t*)import(?: |\t)+([\w|-|\.|,| |\t]*)$', text, re.M|re.I)
      for line in match:
         line = line.split(',')
         modules.update([x.strip() for x in line])

      # from foo import bar
      match = re.findall( r'^(?: *|\t*)from(?: |\t)+((?:\w|-|\.)+)(?: |\t)+import\s+([\w|-|\.|,| |\t]*)$', text, re.M|re.I)
      for line in match:
         line = line[0], line[1].split(',')
         modules.update([line[0]+'.'+x.strip() for x in line[1]])

      # from foo import *
      match = re.findall( r'^(?: *|\t*)from(?: |\t)+((?:\w|-|\.)+)(?: |\t)+import\s+\*$', text, re.M|re.I)
      modules.update(match)



for module in sorted(modules):
   print(module)
