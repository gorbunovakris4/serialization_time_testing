from socket import *
import timeit
import os
import m_pb2


Data = dict(root=dict(int_1=2 ** 9, float_1=3.14, str_1="short string",
                      str_2="I AM LONG STRING, VERY VERY LONG!!!!!!!!!!!!!!!!!!!!",
                      lst_int=[i ** 2 for i in range(1000)],
                      lst_str=[str(i) * 10 for i in range(100)]))


def proto_serialization():
    with open("test.proto", "wb") as f:
        f.write(test.SerializeToString())


def proto_deserialization():
    with open("test.proto", "rb") as f:
        test.ParseFromString(f.read())


if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 2003))
    test = m_pb2.Test()
    test.root.int_1 = Data["root"]["int_1"]
    test.root.float_1 = Data["root"]["float_1"]
    test.root.str_1 = Data["root"]["str_1"]
    test.root.str_2 = Data["root"]["str_2"]
    test.root.lst_int.extend(Data["root"]["lst_int"])
    test.root.lst_str.extend(Data["root"]["lst_str"])
    while True:
        message, address = serverSocket.recvfrom(1024)
        if message == b"get_result":
            time1 = int(timeit.timeit(proto_serialization, timeit.default_timer, number=1000) * 1000)
            time2 = int(timeit.timeit(proto_deserialization, timeit.default_timer, number=1000) * 1000)
            sz = os.path.getsize('test.proto')
            res = f"Google Protocol Buffers - {sz} - {time1}ms - {time2}ms\n"
            serverSocket.sendto(str.encode(res), address)
        else:
            serverSocket.sendto(b"bad request\n", address)
