from elasticsearchReader import ElasticsearchReader
from redisReader import RedisReader
from scan import Scan

if __name__ == '__main__':
	RR = RedisReader( "192.168.30.130" , 6379 )
	S = Scan()
	ip = RR.pop()
	while ip is not None :
		print "ip=",  ip
		S.scanHost( ip )
		ip = RR.pop()

