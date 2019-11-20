# AliDDNS
阿里云域名DDNS自动配置。路由器或者连接路由器的任一电脑运行此脚本均可。

# 使用方法
### 1.安装python和pip
    
    sudo apt install python3 python3-pip
    
### 2.安装阿里云sdk

    pip3 install aliyun-python-sdk-core
    
    pip3 install aliyun-python-sdk-alidns

### 3.申请阿里云AccessKey
从[https://ak-console.aliyun.com/#/accesskey](https://ak-console.aliyun.com/#/accesskey) 申请即可，\<key>参数对应AccessKeyId，\<secret>对应AccessKeySecret

### 4.使用方法 
    查看使用说明
    python3 aliddns.py --help
    自动更新域名IP
    python3 aliddns.py [-h] [--ipv6] <key> <secret> <rr> <domain>
    必选参数:
    key         从https://ak-console.aliyun.com/#/accesskey得到的AccessKeyId
    secret      从https://ak-console.aliyun.com/#/accesskey得到的AccessKeySecret
    rr          例子：@, *, www, ...
    domain      例子: aliyun.com, baidu.com, google.com, ...
    可选参数:
    --ipv6      使用本机的ipv6地址

###### 例子
    python aliddns.py ABDGDJSKN QWERTYUIOPASDG pan baidu.com
    python aliddns.py ABDGDJSKN QWERTYUIOPASDG pan baidu.com --ipv6

### 5.crontab定时执行
    crontab -e
    文件末尾添加一行，功能：每5分钟执行一次
    */5 * * * * python3 /home/xxx/aliddns.py ABDGDJSKN QWERTYUIOPASDG pan baidu.com > /dev/null
    是否成功设置，请在阿里云手动修改后，观察是否自动修改

# 参考项目
[mgsky1/DDNS](https://github.com/mgsky1/DDNS)
