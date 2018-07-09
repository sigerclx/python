# 利用阿里云SDK，取得ECS的各种信息
from aliyunsdkcore.client import AcsClient
import configRead
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
import pprint

def getEcs(account,client):
    
    # 创建 request，并设置参数
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_PageSize(50)

    # 发起 API 请求并打印返回

    response = client.do_action_with_exception(request)
    res=str(response,encoding = "utf-8")
    res= res.replace('true','True')
    res= res.replace('false','False')
    res =eval(res)
    esclist=[]
    line=[]
    #pprint.p    line.append(res["Instances"]["Instance"][0])
    for i in range(len(res["Instances"]["Instance"])):
        line.append(account)
        line.append(res["Instances"]["Instance"][i]['InstanceName'])

        #机器名
        #line.append(res["Instances"]["Instance"][i]['HostName'])

        #一个是默认公网ip,一个是默认EIP
        
        # IS EIP
        if len(res["Instances"]["Instance"][i]['PublicIpAddress']['IpAddress'])<1:
            line.append(res["Instances"]["Instance"][i]['EipAddress']['IpAddress'])
            line.append(res["Instances"]["Instance"][i]['EipAddress']['Bandwidth'])
            
        # 公网IP
        if len(res["Instances"]["Instance"][i]['EipAddress']['IpAddress'])<1:
            tmp=str(res["Instances"]["Instance"][i]['PublicIpAddress']['IpAddress']).strip('[\'')
            tmp=tmp.strip('\']')                                                                          
            line.append(tmp)
            line.append(res["Instances"]["Instance"][i]['InternetMaxBandwidthOut'])
            #line.append(res["Instances"]["Instance"][i]['PublicIpAddress']['IpAddress'])
            

        line.append(res["Instances"]["Instance"][i]['NetworkInterfaces']['NetworkInterface'][0]['PrimaryIpAddress'])
        
       
        line.append(res["Instances"]["Instance"][i]['Cpu'])
        line.append(res["Instances"]["Instance"][i]['Memory'])
        
        line.append(res["Instances"]["Instance"][i]['ExpiredTime'][:10])
        
        #line.append(res["Instances"]["Instance"][i]['InstanceNetworkType'])
        line.append(res["Instances"]["Instance"][i]['InstanceType'])
        
        line.append(res["Instances"]["Instance"][i]['OSName'])
        #line.append(res["Instances"]["Instance"][i]['OSType'])
        #line.append(res["Instances"]["Instance"][i]['RegionId'])
        #line.append(res["Instances"]["Instance"][i]['SaleCycle'])
        line.append(res["Instances"]["Instance"][i]['Status'])
        line.append(res["Instances"]["Instance"][i]['ZoneId'])
        line.append(res["Instances"]["Instance"][i]['Recyclable'])
        #line.append(res["Instances"]["Instance"][i]['VpcAttributes']['PrivateIpAddress']['IpAddress'])
        esclist.append(line)
        line=[]
    return esclist


def getAllaccountEcslist():
    account=configRead.readConfig('aliyun','account')
    ecslist=[]
    ecslists=[]

    for i in account:
        print(account[i])
        for j in account[i][2]:
            #client= AcsClient("LTAInYu7Dfx1S4P5","0pbGDxkQcB1AFPl7u5PXaZgas4MyAo","cn-hongkong")
            client= AcsClient(account[i][0],account[i][1],j)
            ecslist=getEcs(i,client)
            ecslists = ecslists + ecslist
            ecslist=[]
    return ecslists
