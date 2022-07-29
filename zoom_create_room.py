import csv

result = ['Pre-assign Room Name,Email Address\n']

with open('shuo_room.csv', 'r') as f:
    rd = csv.reader(f)
    next(rd)
    for res in rd:
        result.append('Shuo-Ru Room,'+str(res[1])+'\n')

with open('daniel_room.csv', 'r') as f:
    rd = csv.reader(f)
    next(rd)
    for res in rd:
        result.append('Daniel Room,'+str(res[1])+'\n')

with open('eric_room.csv', 'r') as f:
    rd = csv.reader(f)
    next(rd)
    for res in rd:
        result.append('Eric Room,'+str(res[1])+'\n')

with open('zoom_room.csv', 'w') as f:
    for s in result:
        f.write(s)