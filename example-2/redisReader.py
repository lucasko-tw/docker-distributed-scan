import sys
import redis
reload(sys)
sys.setdefaultencoding('utf-8')


class RedisReader ():
    rr = None
    def __init__(self , redis_host , redis_port):

	self.rr = redis.Redis(host=redis_host ,port=int(redis_port),db=0)


    def pop(self):
	ip = self.rr.lpop("ip")
	print "pop ip:" , ip
	return ip

    def push(self , ip ):
	print "push ip:" , ip
        self.rr.lpush("ip", ip)      



if __name__ == "__main__":

 ipList = ['8.8.8.8' , '127.0.0.1']
 rr = RedisReader("127.0.0.1","6379")
 for ip in ipList:
  rr.push(ip)
  #print rr.pop()

