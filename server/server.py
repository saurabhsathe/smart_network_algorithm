import grpc
from concurrent import futures
import time

import file_transfer_pb2_grpc
import file_transfer_pb2
import zlib
import file_transfer
"""
message FileTransferStart{
  string clientip=1;
  string filename=2;
}
"""
class FileTransferService(file_transfer_pb2_grpc.FileTransferServiceServicer):

    client_filemap={}
    def __init__(self,server_configs=4000000):
        self.server_configs=server_configs

    def file_transfer(self, request, context):
        response=file_transfer_pb2.Response()
        #print(request.clientip)
        try:
            if request.clientip not in FileTransferService.client_filemap or FileTransferService.client_filemap[request.clientip]==None:
                response.error=True
                return response

            if file_transfer.file_transfer(request.content,FileTransferService.client_filemap[request.clientip]):
                response.error=False
                return response
            else:
                response.error=True
                return response
        except Exception as e:
            print("facing some issue due to ", e)

    def ServerResponse(self, request, context):
        response=file_transfer_pb2.ServerSpeedResponse()
        response.server_mtu=self.server_configs
        return response

    def OptimizeStart(self,request,context):
        response=file_transfer_pb2.Response()
        file_transfer.optimize_start()



    def OptimizeEnd(self,request,context):
        response=file_transfer_pb2.Response()
        file_transfer.optimize_end()
        return response

    def OptimizerFileTransfer(self,request,context):
        response=file_transfer_pb2.Response()

        if file_transfer.optimize_network(request.content):
            response.error=False
            return response
        else:
            response.error=True
            return response

    def TransferFileStart(self, request, context):
        FileTransferService.client_filemap[request.clientip]=request.filename
        response=file_transfer_pb2.GeneralMessage()
        response.content="No error"
        response.clientip=request.clientip
        return response
    def TransferFileEnd(self, request, context):
        FileTransferService.client_filemap[request.clientip]=None
        response=file_transfer_pb2.GeneralMessage()
        response.content="No error"
        response.clientip=request.clientip
        return response


def serve(mx_srv_len=4000000):
    max_server_message_length=mx_srv_len
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4),options=[('grpc. max_receive_message_length', max_server_message_length),('grpc. max_send_message_length', max_server_message_length)])
    #print(dir(grpc.server.__defaults__))
    #print(grpc.server.__defaults__)
    file_transfer_pb2_grpc.add_FileTransferServiceServicer_to_server(FileTransferService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
serve()