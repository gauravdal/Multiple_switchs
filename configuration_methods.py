def trunk_func(interface_num):
    trunk_config = [
        'interface ' + interface_num,
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport nonegotiate',
        'switchport trunk allowed vlan all'
    ]
    return trunk_config