# AliDDNS
阿里云域名DDNS自动配置

# 使用方法
### 1.安装python和pip
    
    sudo apt install python3 python3-pip
    
### 2.安装阿里云sdk

    pip3 install aliyun-python-sdk-core
    
    pip3 install aliyun-python-sdk-alidns

### 3.申请阿里云AccessKey
从[https://ak-console.aliyun.com/#/accesskey](https://ak-console.aliyun.com/#/accesskey) 申请即可，\<key>参数对应AccessKeyId，\<secret>对应AccessKeySecret

### 4.使用方法
    python3 aliddns.py <key> <secret> <rr> <domain> [--ipv6]
###### 例子
    python aliddns.py ABDGDJSKN QWERTYUIOPASDG pan baidu.com
    python aliddns.py ABDGDJSKN QWERTYUIOPASDG pan baidu.com --ipv6

### 5.crontab定时执行
    crontab -e
    文件末尾添加一行，功能：每5分钟执行一次
    */5 * * * * python3 /home/xxx/aliddns.py ABDGDJSKN QWERTYUIOPASDG pan baidu.com
    是否成功设置，请在阿里云手动修改后，观察是否自动修改

# 参考项目
[mgsky1/DDNS](https://github.com/mgsky1/DDNS)