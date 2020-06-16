#!/usr/bin/env python
# coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from  aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
import urllib.request
import json
import time
import argparse

# 利用API获取IP
def getRealIp():
    url = "https://api.ipify.org/?format=json"
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    jsonData = json.loads(html)
    return jsonData['ip']

# 利用API获取IP
def getRealIpV6():
    url = "https://v6.ident.me/"
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html

def getRecords(client,rr,domain):
    request= DescribeDomainRecordsRequest()
    request.set_accept_format('json')
    request.set_DomainName(domain)
    request.set_RRKeyWord(rr)
    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))
    jsonData = json.loads(response)
    return jsonData['DomainRecords']['Record']

def addDomainRecord(client,rr,domain,ip,type):
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Value(ip)
    request.set_Type(type)
    request.set_RR(rr)
    request.set_DomainName(domain)
    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))
    return json.loads(response)['RecordId']

def updateDomainRecord(client,rr, domain, ip, type):
    records = getRecords(client,rr,domain)
    record_id=None
    for record in records:
        if record['RR'] == rr and record['DomainName']==domain and record['Type']==type:
            record_id=record['RecordId']
            avail_ip=record['Value']
            avail_record=record
            break
    if record_id is None:
        print("不存在记录，正在添加记录")
        addDomainRecord(client,rr,domain,ip,type)
    else:
        print("存在记录："+str(avail_record))
        if avail_ip==ip:
            print("ip未改变，不更改记录，原ip="+avail_ip+"，现ip="+ip)
        else:
            print("ip已改变，准备更改记录，原ip="+avail_ip+"，现ip="+ip)
            request=UpdateDomainRecordRequest()
            request.set_action_name("UpdateDomainRecord")
            request.set_RR(rr)
            request.set_RecordId(record_id)
            request.set_Type(type)
            request.set_Value(ip)
            request.set_TTL(600)
            request.set_accept_format('json')
            response = client.do_action_with_exception(request)
            print(str(response, encoding='utf-8'))
            return json.loads(response)['RecordId']

#updateDomainRecord('pan4','quancs.site',getRealIp())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description = '阿里云云解析工具'
    parser.add_argument("key", help="从https://ak-console.aliyun.com/#/accesskey得到的AccessKeyId", type=str)
    parser.add_argument("secret", help="从https://ak-console.aliyun.com/#/accesskey得到的AccessKeySecret", type=str)
    parser.add_argument("rr",help="RR例子：@, *, www, ...", type=str)
    parser.add_argument("domain", help="domain例子: aliyun.com, baidu.com, google.com, ...", type=str)
    parser.add_argument("--ipv6", help="使用本机的ipv6地址",action="store_true")
    args = parser.parse_args()
    if args.ipv6:
        ip=getRealIpV6()
        type="AAAA"
    else:
        ip=getRealIp()
        type="A"
    print("本机IP: " + ip)

    client = AcsClient(args.key, args.secret, 'cn-hangzhou')
    updateDomainRecord(client,args.rr,args.domain,ip,type)