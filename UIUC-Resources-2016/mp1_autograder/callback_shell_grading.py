import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(100)
port = 31337
s.bind(('localhost',port))

s.listen(1)
while True:
    c,addr = s.accept()
    c.send('touch stdin.txt\n')
    c.send('whoami\n')
    data1 = c.recv(1024).strip()
    print data1
    if(data1 != ''):
        c.send('touch stdout.txt\n')
    c.send('abc\n')
    data2 = c.recv(1024).strip()
    if(data2 != ''):
        c.send('touch stderr.txt\n')
    print data2
    c.close()
    
