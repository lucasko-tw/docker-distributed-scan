
### Installation

```
sudo apt-get install python-pip
pip install redis
pip install elasticsearch
```


### Ready
```
docker pull redis

docker run -it --name redis-server -p 6379:6379 -d redis 

docker pull lucasko/elasticsearch

docker run -it --name elasticsearch-server -p 9200:9200 -d lucasko/elasticsearch 

docker pull lucasko/python

```

### Check Redis IP

```
ifconfig

vim app.py
```

```
RR = RedisReader( "192.168.30.130" , 6379 )
```


### Add IP
```
python redisReader.py
```


###
```
docker-compose up
```
