import socket

# making socket and stabilishing connection

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.data.pr4e.org', 80))
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
	# I'll receive 512 characters at time
    data = mysock.recv(512)
    # break when get to the end of the file
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()