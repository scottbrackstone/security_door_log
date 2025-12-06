import re

file_name = 'door_log.txt'
try:
    fhandle = open(file_name)
except:
    print("File not found.")
    quit()

hour_count = dict()
name_count = dict()

for line in fhandle:
    line = line.rstrip()
    hours = re.findall(r'^\[([0-9]+):', line)
    if len(hours) > 0:
        hours = int(hours[0])
        hour_count[hours] = hour_count.get(hours, 0) + 1

    names = re.findall(r'<(\S+)>', line)
    if len(names) > 0:
        names = names[0]
        name_count[names] = name_count.get(names, 0) + 1

name_list = list()
hours_list = list()

for hours, count in hour_count.items():
    hour_tup = count, hours
    hours_list.append(hour_tup)
hours_list.sort(reverse=True)

highest_hour = hours_list[0]
count, hour = highest_hour
print("The busiest hour was:", hour, "o'clock, with", count, "visits.")

for name, count in name_count.items():
    name_tup = count, name
    name_list.append(name_tup)
name_list.sort(reverse=True)

highest_name = name_list[0]
count, name = highest_name
print("The person with the most visits was", name, "with", count, "visits.")