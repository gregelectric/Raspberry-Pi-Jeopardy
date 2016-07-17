import getpass
import sys
import telnetlib
import time

tn = telnetlib.Telnet("10.0.1.44")

tn.read_until("Please input username and password!")
tn.write("admin=admin\n")
tn.read_until("Username and password is ok!")

while True:
    tn.write("setpower=00010000\n")
    time.sleep(1)
    tn.write("setpower=00100000\n")
    time.sleep(1)
    tn.write("setpower=01000000\n")
    time.sleep(1)
    tn.write("setpower=10000000\n")
    time.sleep(1)
    tn.write("setpower=01000000\n")
    time.sleep(1)
    tn.write("setpower=00100000\n")
    time.sleep(1)


