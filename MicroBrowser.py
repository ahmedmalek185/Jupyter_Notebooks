#import urllib.request, urllib.parse, urllib.error
#fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
#for line in fhand:
#    print(line.decode().strip())

#OR
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
