from socket import *
import timeit
import os
import json


Data = dict(root=dict(int_1=2 ** 9, float_1=3.14, str_1="short string",
                      str_2="I AM LONG STRING, VERY VERY LONG!!!!!!!!!!!!!!!!!!!!",
                      lst_int=[i ** 2 for i in range(1000)],
                      lst_str=[str(i) * 10 for i in range(100)]))


def json_serialization():
    with open("test.json", "w") as f:
        json.dump(Data, f)


def json_deserialization():
    with open("test.json", "r") as f:
        json.load(f)


if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 2002))
    while True:
        message, address = serverSocket.recvfrom(1024)
        if message == b"get_result":
            time1 = int(timeit.timeit(json_deserialization, timeit.default_timer, number=1000) * 1000)
            time2 = int(timeit.timeit(json_deserialization, timeit.default_timer, number=1000) * 1000)
            sz = os.path.getsize('test.json')
            res = f"JSON - {sz} - {time1}ms - {time2}ms\n"
            serverSocket.sendto(str.encode(res), address)
        else:
            serverSocket.sendto(b"bad request\n", address)
