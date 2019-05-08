"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
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
        i[2].split('-')[1]
#         print(1)
        if i[0] not in time_of_num.keys():
            time_of_num[i[0]] = 0
        else:
            time_of_num[i[0]] = int(i[3])
key = max(time_of_num)
value = max(time_of_num.values()) 
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key,value))


