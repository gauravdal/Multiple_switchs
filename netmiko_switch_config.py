from netmiko import ConnectHandler

ios_l2_s1 = {
    'device_type' : 'cisco_ios',
    'ip':'192.168.1.1',
    'username':'gaurav',
    'password': 'VIRL'
}

ios_l2_s2 = {
    'device_type' : 'cisco_ios',
    'ip':'192.168.1.2',
    'username':'gaurav',
    'password': 'VIRL'
}

ios_l2_s3 = {
    'device_type' : 'cisco_ios',
    'ip':'192.168.1.3',
    'username':'gaurav',
    'password': 'VIRL'
}

ios_l2_s4 = {
    'device_type' : 'cisco_ios',
    'ip':'192.168.1.4',
    'username':'gaurav',
    'password': 'VIRL'
}

ios_l2_s5 = {
    'device_type' : 'cisco_ios',
    'ip':'192.168.1.5',
    'username':'gaurav',
    'password': 'VIRL'
}

ios_l2_s6 = {
    'device_type' : 'cisco_ios',
    'ip':'192.168.1.6',
    'username':'gaurav',
    'password': 'VIRL'
}




switches_list = [ios_l2_s1, ios_l2_s2, ios_l2_s3, ios_l2_s4, ios_l2_s5,ios_l2_s6]

for each_switch in switches_list:
    net_connect = ConnectHandler(**each_switch)
    output = net_connect.send_command('show ip int brief')
    print(output)

    config_commands = ['int loop 0','ip address 1.1.1.1 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)

    for n in range(2,12):
        print('Creating vlan '+str(n))
        config_commands = ['vlan '+str(n),'name netmiko_vlan_'+str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
    net_connect.send_command('wr')
