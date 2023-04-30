import pickle
from socket import *
import timeit
import os

Data = dict(root=dict(int_1=2 ** 9, float_1=3.14, str_1="short string",
                      str_2="I AM LONG STRING, VERY VERY LONG!!!!!!!!!!!!!!!!!!!!",
                      lst_int=[i ** 2 for i in range(1000)],
                      lst_str=[str(i) * 10 for i in range(100)]))


def pickle_serialization():
    with open("test.pickle", "wb") as f:
        pickle.dump(Data, f)


def pickle_deserialization():
    with open("test.pickle", "rb") as f:
        pickle.load(f)


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 2001))
    while True:
        message, address = serverSocket.recvfrom(1024)
        if message == b"get_result":
            time1 = int(timeit.timeit(pickle_serialization, timeit.default_timer, number=1000) * 1000)
            time2 = int(timeit.timeit(pickle_deserialization, timeit.default_timer, number=1000) * 1000)
            sz = os.path.getsize('test.pickle')
            res = f"Pickle - {sz} - {time1}ms - {time2}ms\n"
            serverSocket.sendto(str.encode(res), address)
        else:
            serverSocket.sendto(b"bad request\n", address)
