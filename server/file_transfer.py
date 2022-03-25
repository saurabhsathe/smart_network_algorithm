import os
import zlib

def file_transfer(bytes,filename="sample.dat"):
    encoding="utf-8"
    try:
        #print("in the server",bytes)
        f = open(filename, "a")
        #bytes=zlib.decompress(bytes)
        bytes_decoded=bytes.decode(encoding)
        f.write(bytes_decoded)
        f.close()
        return True
    except Exception as e:
        print(e)
        return False

def optimize_network(bytes):
    encoding="utf-8"
    try:
        f = open("demofile.txt", "a")
        #bytes=zlib.decompress(bytes)
        bytes_decoded=bytes.decode(encoding)
        f.write(bytes_decoded)
        f.close()
        return True
    except Exception as e:
        print(e)
        return False

def optimize_start():
    try:
        f=open("demofile.txt","w")
        f.close()
    except Exception as e:
        print(e)
def optimize_end():
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")