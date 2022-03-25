import grpc
import file_transfer_pb2
import file_transfer_pb2_grpc
import time
import psutil
import pandas as pd
import zlib
def get_optimal_chunk(stub):
    req=file_transfer_pb2.ServerSpeedRequest()
    req.request=1
    resp=stub.ServerResponse(req)
    print(resp)
    max_mtu=resp.server_mtu
    ans=[]
    try:
        count=0
        chunk_size=1000000
        curr=float("-inf")
        optimal_chunk_size=-1
        while count<1000 and chunk_size<max_mtu:
            data = str.encode("#"*chunk_size)#zlib.compress()
            req=file_transfer_pb2.Request()
            req.chukid=1
            req.content=data
            t1=time.time()
            resp= stub.OptimizerFileTransfer(req)#stub.file_transfer(req)
            t2=time.time()
            latency=(t2-t1)*1000000
            if latency==0:
                count+=1
                continue

            throughput=(chunk_size)/latency
            #print("throughput observed is",throughput,chunk_size)
            if throughput>=curr:
                curr=throughput
                optimal_chunk_size=chunk_size
            chunk_size+=8000
            count+=1
            ans.append((chunk_size,throughput))
        print("optimal_chunk_size and optimal throughput is ",optimal_chunk_size,curr)
        resp=stub.OptimizeEnd(file_transfer_pb2.GeneralMessage())
        #df=pd.DataFrame(ans).to_csv("thread1.csv")
        return optimal_chunk_size,curr
    except Exception as e:
        print("Filure experienced due to",e)
        return None
"""
if __name__=="__main__":
    channel=grpc.insecure_channel('localhost:50051')
    stub=file_transfer_pb2_grpc.FileTransferStub(channel)
    response=client(stub)
    t1=time.time()
    print(psutil.net_if_stats()['Wi-Fi'].mtu)
    #print(psutil.net_if_stats().keys())
    print(response)

"""