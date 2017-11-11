from elasticsearch import Elasticsearch
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

class ElasticsearchReader ():
    client = None
    def __init__(self , host , port):
        url = "%s:%s" % (host , port)
        self.client = Elasticsearch( [url] , send_get_body_as="POST")

    def deleteIndex(self , esIndex):
	if self.client.indices.exists(index= esIndex ):
		self.client.indices.delete(index=esIndex, ignore=[400, 404])

    def saveJson(self , esIndex , esType , json):
        
        res = self.client.index(index=esIndex, doc_type=esType , body=json)
        return res

if __name__ == "__main__":
  
  er = ElasticsearchReader("127.0.0.1" , 9200)
  user = {"name": "lucasko" , "age":18 }
  er.saveJson("test" , "user" , user)

