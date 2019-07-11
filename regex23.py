import re

str = "The ain in ains"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


