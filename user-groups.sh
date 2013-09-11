#!/bin/bash
while read line ; do
  primary_group_id=`echo $line |awk -F: '{print $4}'`
  username=`echo $line |awk -F: '{print $1}'`
  primary_group=`grep -w $primary_group_id /etc/group |awk -F: '{print $1}'`
  echo -----------------------------------------------------------------
  echo name:$username primary group:$primary_group
  echo other groups:
  grep -w $username /etc/group |awk -F: '{print "\t"$1}'
done < /etc/passwd
