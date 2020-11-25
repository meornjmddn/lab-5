import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


addr = ("192.168.68.111",8888)

s.sendto(b'Hi, saya client. Terima Kasih!',addr)

data = s.recvfrom(1024)
print (data)

s.close()
