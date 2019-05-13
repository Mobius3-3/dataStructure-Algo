"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
### running time analysis:  O(n)

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
time_of_num = {}
for i in calls:
    if (i[2].split('-')[1] =="09" and i[2].split('-')[2][:4] == "2016"):
        time_of_num[i[0]] = time_of_num[i[0]]+int(i[3]) if i[0] in time_of_num.keys() else int(i[3])
        time_of_num[i[1]] = time_of_num[i[1]]+int(i[3]) if i[1] in time_of_num.keys() else int(i[3])
key = max(time_of_num, key=time_of_num.get)
value = time_of_num[key] 
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key,value))


