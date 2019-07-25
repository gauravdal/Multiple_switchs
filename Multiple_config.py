import getpass
import telnetlib

host = 'HOST'
user = input('Enter the username for login: ')
password = getpass.getpass()

#opening file of ip addresses of switches
fout = open('switches_ip.txt','r')

for host in fout:
    host = host.strip()
    ip = host
    print('Writing into switch: '+ str(ip))
    tn = telnetlib.Telnet(ip)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b'enable\n')
    tn.write(b'cisc0\n')
    tn.write(b'config t\n')
    for n in range(2,10):
        tn.write(b'vlan ' +str(n).encode('ascii')+b'\n')
        tn.write(b'name Python_vlan_' + str(n).encode('ascii') + b'\n')

    tn.write(b'end\n')
    tn.write(b'wr\n')
    tn.write(b'exit\n')
    print(tn.read_all().decode('ascii'))
