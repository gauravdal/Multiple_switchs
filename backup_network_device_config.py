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
    print('Getting running config from switch: '+ str(ip))
    tn = telnetlib.Telnet(ip)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b'enable\n')
    tn.write(b'cisc0\n')
    tn.write(b'terminal length 0\n')
    tn.write(b'show run\n')
    tn.write(b'exit\n')

    ReadOutput = tn.read_all()
    SaveOutput = open('switch_'+ip, 'w')
    SaveOutput.write(ReadOutput.decode('ascii'))
    SaveOutput.write('\n')
    SaveOutput.close()