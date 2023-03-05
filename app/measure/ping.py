import os

hostname = "127.0.0.1"
response = os.system("ping " + hostname) # ping 127.0.0.1

if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')
