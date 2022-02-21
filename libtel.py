import getpass
import telnetlib
import time

host = "172.31.103.4"
user =  input("Enter username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host, 23, 10)

tn.read_until(b"Username")
tn.write(user.encode('ascii') + b"\n")
time.sleep(1)

tn.read_until(b"Password:")
tn.write(password.encode('ascii') + b"\n")
time.sleep(1)
tn.write(b"config ter\n")
time.sleep(1)
tn.write(b"interface gigabit0/1\n")
time.sleep(1)
tn.write(b"ip address 172.31.103.17 255.255.255.240\n")
time.sleep(2)
tn.write(b"do show ip int br\n")
time.sleep(2)
tn.write(b"exit\n")
time.sleep(1)

output = tn.read_very_eager()
print(output.decode('ascii'))

tn.close()