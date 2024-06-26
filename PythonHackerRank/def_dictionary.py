from collections import defaultdict
d = defaultdict(list)
d['name'].append('Adam')
d['parents'].append('Sherin')
d['parents'].append('Sharvan')
d['age'].append(2)

for key in d.keys():
    print(d[key])