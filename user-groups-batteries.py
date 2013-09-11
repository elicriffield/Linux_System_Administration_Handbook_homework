#!/usr/bin/python
'''Use the build in libs to access groups and passwords'''

import grp, pwd 

def get_groups(user):
  groups = [g.gr_name for g in grp.getgrall() if user in g.gr_mem]
  gid = pwd.getpwnam(user).pw_gid
  try: 
    groups.append(grp.getgrgid(gid).gr_name)
  except:
    pass
  return groups

for row in pwd.getpwall():
  try:
    group = grp.getgrgid(row.pw_gid).gr_name
  except:
    group = ''

  print('---------------------------------------------------')
  print('name:{0} group:{1}'.format(row.pw_name, group))
  print('other groups:{0}'.format(get_groups(row.pw_name)))
