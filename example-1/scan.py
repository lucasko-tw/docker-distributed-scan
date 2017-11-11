import os,sys


class Scan :

 def scanHost(self , hostname) :

   response = os.system("ping -c 5 " + hostname)

   #and then check the response...
   if response == 0:
     print hostname, 'is up!'
   else:
     print hostname, 'is down!'


if __name__ == '__main__':
  s = Scan()
  s.scanHost( sys.argv[1] )
