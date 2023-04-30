from socket import *
import timeit
import os
import xmltodict

Data = dict(root=dict(int_1=2 ** 9, float_1=3.14, str_1="short string",
                      str_2="I AM LONG STRING, VERY VERY LONG!!!!!!!!!!!!!!!!!!!!",
                      lst_int=[i ** 2 for i in range(1000)],
                      lst_str=[str(i) * 10 for i in range(100)]))


def xml_serialization():
    with open("test.xml", "w") as f:
        xmltodict.unparse(Data, f)


def xml_deserialization():
    with open("test.xml", "r") as f:
        xmltodict.parse(''.join(f.readlines()))


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 2004))
    while True:
        message, address = serverSocket.recvfrom(1024)
        if message == b"get_result":
            time1 = int(timeit.timeit(xml_serialization, timeit.default_timer, number=1000) * 1000)
            time2 = int(timeit.timeit(xml_deserialization, timeit.default_timer, number=1000) * 1000)
            sz = os.path.getsize('test.xml')
            res = f"XML - {sz} - {time1}ms - {time2}ms\n"
            serverSocket.sendto(str.encode(res), address)
        else:
            serverSocket.sendto(b"bad request\n", address)
