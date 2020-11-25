import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Berjaya buat sokett")
port = 8888
s.bind(('', port))
print("Berjaya bind soket di port: " + str(port))
print("soket tengah menunggu client!")

while True:
        c = s.recvfrom(1024)
        buffer = c[0]
        addr = c[1]
        print("Dapat capaian dari: " + str(addr))

        s.sendto(b'Sama sama!',addr)
        print(buffer)
c.close()
