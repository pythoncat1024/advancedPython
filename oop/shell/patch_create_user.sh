#!/usr/bin/env bash
set +x
dirty_list=""

function roll_back(){
    echo "出错了，自动回滚中...."
    samba_config_file='/etc/samba/smb.conf'
    for item in $dirty_list
    do
        # 1. 删除当前用户(包含创建的 /home/$item 目录)
        sudo userdel -r $item
        # 2. 删除 Samba 中的配置信息 (删除文件部分行)
        num=`grep -n "\[$item\]" $samba_config_file | awk '{print $1}' | awk -F ":" '{print $1}'`
        (( last=num+10 ))
        sudo sed -i "$num,$lastd" $samba_config_file
    done
    if [ -f $samba_config_file".bak" ];then
        sudo rm -rf $samba_config_file
        sudo mv $samba_config_file".bak" $samba_config_file
    fi

}
function add_samba() {
    # 添加 Samba 用户
   #利用echo -e 的回车功能解决 smbpasswd 需要交互的问题，比expect简单多了
   echo -e "$1\n$1" | sudo smbpasswd -a $1 -s
   echo "add $1 in Samba ok"
   if [ 0 -ne "$?" ];then
        roll_back
   fi
}

function config_samba(){
    samba_config_file='/etc/samba/smb.conf'
    if [ -f $samba_config_file ];then
        echo "" > /dev/null
        sudo cp $samba_config_file $samba_config_file.bak
    else
        echo "Samba 配置文件不存在，请确认Samba 是否已经正确安装！！！"
        roll_back
        exit 3
    fi
    old_permission=`stat -c %a $samba_config_file`
    sudo chmod 777 $samba_config_file # 必须这样做，不然就不能修改，尴尬！！！
   (
    sudo cat << EOF

[$1]
comment = Share Folder
browseable = yes
path = /home/$1
create mask = 0644
directory mask = 0755
valid users = $1
public = yes
writable = yes
available = yes
EOF
    ) >>  $samba_config_file
    sudo chmod $old_permission $samba_config_file
}


function create_user(){
    # 创建 帐号(linux 用户)
    name=$1
    pass=$name
    sudo useradd -m $name -d /home/$name -s /bin/bash
    if [ $? -eq 0 ];then
       echo "user ${name} is created successfully!!!" > /dev/null
    else
       echo "user ${name} is created fail!!!"
       roll_back
       exit 6
    fi
    echo "$name:$pass" | sudo chpasswd
    rm -rf user.txt
    if [ $? -eq 0 ];then
       echo "${name}'s password is set successfully" > /dev/null
    else
       echo "${name}'s password is set fail!!!"
       roll_back
       exit 4
    fi
}

############### execute ##############################################

echo "############### start execute ##############################################"

if [ "$#" -le 0 ]; then
    echo "nothing happened!"
    echo "please input the future user names, if you want add users"
    exit 1
fi

echo "将要创建以下用户(用户名和密码相同):"$@
read -p "是否确定要创建这些用户[Y/n]? "

echo "REPLY==="$REPLY
if [ "y"=$RELPY ] || [ "Y"=$RELPY ];then
    echo "正在创建用户...."
else
    echo "已取消"
    exit 2
fi

for item in $@
do
    grep $item /etc/pssswd >& /dev/null
    if [ 0 -eq "$?" ];then
        echo "$item 用户已经存在..."
        continue
    fi
    dirty_list=$dirty_list" "$item
    create_user $item
    add_samba $item
    config_samba $item
done
sudo /etc/init.d/samba restart
