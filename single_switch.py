from netmiko import ConnectHandler
from configuration_method import trunk_func

ios_l2_s1 = {
    'device_type' : 'cisco_ios',
    'ip':'192.168.1.1',
    'username':'gaurav',
    'password': 'VIRL'
}
switches_list = [ios_l2_s1]

for each_switch in switches_list:
    net_connect = ConnectHandler(**each_switch)
    output = net_connect.send_command('show ip int brief')
    print(output)



    # Making trunk configuration
    user_input = input('Do you want to add configuration of trunk lines in switches,(yes/No): ')
    while (user_input == 'yes'):
        interface_num = input('Taking interface number, example(g0/0,g0/1): ')

        net_connect.send_config_set(trunk_func(interface_num))
        print(net_connect.find_prompt())

        user_input = input('Do you want to add configuration of trunk lines in switches,(yes/No): ')
