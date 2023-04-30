# serialization_time_testing

## Description

Project testing serialization and deserialization time for exactly same data structure using Google Protocol Buffers, YAML, JSON, XML, Apache Avro, MessagePack and default for Python - Pickle.

## Usage

### 1. From the root of the project build all the containers 

```bash
docker build -t pickle_tst:1.0 ./pickle

docker build -t json_tst:1.0 ./json

docker build -t proto_tst:1.0 ./proto

docker build -t xml_tst:1.0 ./xml

docker build -t avro_tst:1.0 ./avro

docker build -t mpk_tst:1.0 ./mpk
 
docker build -t yaml_tst:1.0 ./yaml 
```

### 2. Run all the containers with docker compose:

```bash
docker compose up -d
```

### 3. Send message "get_result" to the port 2001-2007 depending on the format:

|        **Format**       | **UDP Port** |
|:-----------------------:|:------------:|
|          Pickle         |     2001     |
|           JSON          |     2002     |
| Google Protocol Buffers |     2003     |
|           XML           |     2004     |
|       Apache Avro       |     2005     |
|       MessagePack       |     2006     |
|           YAML          |     2007     |

In less than a minute you will receive answer in format

{format} - {serialized structure file size in bytes} - {time of serialization in ms} - {time of deserialization in ms}


### 4. Examples

Example of the request

```bash
echo -n "get_result" | nc -4u localhost 2001
```

Example of the response

```bash
Pickle - 6842 - 99ms - 45ms
```

## Data structure

Testing data structure contains several types

```python
Data = dict(root=dict(int_1=2 ** 9, float_1=3.14, str_1="short string",
                      str_2="I AM LONG STRING, VERY VERY LONG!!!!!!!!!!!!!!!!!!!!",
                      lst_int=[i ** 2 for i in range(1000)],
                      lst_str=[str(i) * 10 for i in range(100)]))

```
