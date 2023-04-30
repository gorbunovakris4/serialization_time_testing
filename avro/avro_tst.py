from socket import *
import timeit
import os
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


Data = dict(root=dict(int_1=2 ** 9, float_1=3.14, str_1="short string",
                      str_2="I AM LONG STRING, VERY VERY LONG!!!!!!!!!!!!!!!!!!!!",
                      lst_int=[i ** 2 for i in range(1000)],
                      lst_str=[str(i) * 10 for i in range(100)]))


def avro_serialization():
    writer = DataFileWriter(open("test.avro", "wb"), DatumWriter(), schema)
    writer.append(Data)
    writer.close()


def avro_deserialization():
    DataFileReader(open("test.avro", "rb"), DatumReader())


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 2005))
    schema = avro.schema.parse(open("m.avsc", "rb").read())
    while True:
        message, address = serverSocket.recvfrom(1024)
        if message == b"get_result":
            time1 = int(timeit.timeit(avro_serialization, timeit.default_timer, number=1000) * 1000)
            time2 = int(timeit.timeit(avro_deserialization, timeit.default_timer, number=1000) * 1000)
            sz = os.path.getsize('test.avro')
            res = f"Apache Avro - {sz} - {time1}ms - {time2}ms\n"
            serverSocket.sendto(str.encode(res), address)
        else:
            serverSocket.sendto(b"bad request\n", address)
