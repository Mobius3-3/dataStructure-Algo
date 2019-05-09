"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
all=[]
outer = []

for i in calls:
    all.append(i[0])
    outer.append(i[1])
for i in texts:
    outer.append(i[0])
    outer.append(i[1])

                    

print("These numbers could be telemarketers: \n")

for i in sorted(list(set(all)-set(outer))):
  print(i+'\n')

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

