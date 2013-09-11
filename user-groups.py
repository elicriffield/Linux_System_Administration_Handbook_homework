#!/usr/bin/python
'''Do it in pure python with no libraries'''
groups = {}
group_by_id = {}
with open('/etc/group') as grpfd:
  for line in grpfd:
    line = line.split(':')
    groups[line[0]] = line[3].strip().split(',')
    group_by_id[line[2]] = line[0]

with open('/etc/passwd') as pasfd:
  for line in pasfd:
    line = line.split(':')
    username = line[0]
    group = group_by_id[line[3]]
    print('\n-----------------------------')
    print('name:{0}, group:{1}'.format(username, group))
    allgroups = []
    for group in groups.keys():
      if username in groups[group]:
        allgroups.append(group)
    print('other groups:{}'.format(allgroups))

