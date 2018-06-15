#!/usr/bin/env bash

# 改编自：https://zhangge.net/5102.html
#批量添加用户
add_list(){
    #从参数中读取用户帐号并循环添加
    for username in $@
    do
        #利用echo -e 的回车功能解决 smbpasswd 需要交互的问题，比expect简单多了
        echo -e "$username\n$username" | smbpasswd -a $username -s

    done
}
#单个添加用户
add_samba() {
   #利用echo -e 的回车功能解决 smbpasswd 需要交互的问题，比expect简单多了
   echo -e "$1\n$1" | sudo smbpasswd -a $1 -s
}

add_samba $1