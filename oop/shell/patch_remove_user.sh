#!/usr/bin/env bash

echo "将要删除的用户："$@
read -p "是否确定要删除这些用户[Y/n]? "

if [ "y"=$RELPY ] || [ "Y"=$RELPY ];then
    :
else
    echo "执行前取消。 nothing happened~"
    exit 2
fi
for user in $@
do
    echo "delete $user now ....."
    userdel -r $user
    smbpasswd -x $user
    echo "delete $user success..."
done