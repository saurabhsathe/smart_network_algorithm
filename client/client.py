import grpc
import file_transfer_pb2
import file_transfer_pb2_grpc
import time
import get_optimal_chunksize
import pandas as pd
#import zlib

def client(stub,chunksize,opt_through,fname,clientid="192.168.0.0"):
    with open(fname, mode='rb') as file:
        chunk_size=1000000 if chunksize==None else chunksize
        def get_data(file):
            while True:
                data = file.read(chunk_size)
                #data=zlib.compress(data)
                if not data:
                    break
                yield data
        count=1
        streak=0
        ans=[]

        for piece in get_data(file):
            #print(piece)
            req=file_transfer_pb2.Request()
            req.chukid=count
            req.content=piece
            req.clientip=clientid
            t1=time.time()
            resp=stub.file_transfer(req)
            t2=time.time()
            if (t2-t1)!=0:
                minutes=int(t2/60)
                seconds = int(t2 % 60)

                latency=(t2-t1)*1000000
                thru=chunk_size/latency
                if thru>1.20*opt_through:
                    streak+=1
                elif thru<0.8*opt_through:
                    streak-=1
                if streak==5:
                    print("increasing the chunksize")
                    streak=0
                    chunk_size+=8000
                    opt_through=thru
                    ans.append((minutes+seconds,chunk_size))
                elif streak==-5:
                    print("reducing the chunksize")
                    streak=0
                    chunk_size-=8000
                    opt_through=thru
                    ans.append((minutes+seconds,chunk_size))
            else:
                time.sleep(1)

            count+=1
            #print(resp)
    pd.DataFrame(ans).to_csv("time_series_packetsize.csv",index=False)
    return True


def transfer_file(stub,chunksize,opt_through,filename):

    clientip="192.168.1.120"
    req=file_transfer_pb2.FileTransferStart()
    req.clientip=clientip
    req.filename=filename

    t1=time.time()
    resp=stub.TransferFileStart(req)
    resp=client(stub,chunksize,opt_through,filename,"192.168.1.120")

    t2=time.time()
    print("File transfer completed at ",(t2-t1))
    return (t2-t1)

if __name__=="__main__":
    filename= "sales_records.csv"
    channel=grpc.insecure_channel('localhost:50051')
    stub=file_transfer_pb2_grpc.FileTransferServiceStub(channel)
    chunksize,opt_through=get_optimal_chunksize.get_optimal_chunk(stub)
    response=transfer_file(stub,chunksize,opt_through,filename)



#49845.58081626892 for 1500
#3057.1300983428955