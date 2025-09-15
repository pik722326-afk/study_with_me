#Номер 13
'''
# Номер 13 https://education.yandex.ru/ege/task/b6ff76ad-5608-4e7d-833d-dced5a6e2479
from ipaddress import *
for mask in range(1, 32+1):
    net = ip_network(f"111.81.27.208/{mask}", 0)
    print (net, net.netmask)
# Ответ-192,  111.81.27.192
'''
#13 задание Школа
"""
'''from ipaddress import *
cnt = 0
net = ip_network('192.168.32.176/255.255.255.240', 0)
for ip in net:
    if f'{ip:b}'.count('1') % 2 != 0:
        cnt += 1
print(cnt)'''#Answer: 8

'''from ipaddress import *
R = []
net = ip_network('191.128.66.83/255.192.0.0', 0)
print(net[-2])'''#Answer: 191.191.255.254

'''from ipaddress import *
cnt = 0
net = ip_network('252.67.33.87/255.248.0.0', 0)
for ip in net:
    if f'{ip:b}'[16:].count('1') / f'{ip:b}'[:16].count('1') > 2:
        cnt += 1
print(cnt)'''#Answer: 17
'''from ipaddress import *
net = ip_network('45.172.106.203/255.255.252.0', 0)
print(net[-2])'''#Answer: 45.172.107.254
'''from ipaddress import *
cnt = 0
net = ip_network('172.16.192.0/255.255.192.0', 0)
for ip in net:
    if f'{ip:b}'.count('1') % 5 != 0:
        cnt += 1
print(cnt)'''#Answer: 13003
'''from ipaddress import *
cnt = 0
net = ip_network('192.168.160.0/255.255.224.0', 0)
for ip in net:
    if f'{ip:b}'.count('1')==19:
        cnt+=1
print(cnt)'''#Answer: 13
'''from ipaddress import *
cnt = 0
net = ip_network('123.222.0.192/255.255.255.224', 0)
for ip in net:
    if f'{ip:b}'.count('0') == f'{ip:b}'.count('1'):
        cnt += 1
print(cnt)'''#Answer: 10
'''from ipaddress import *
cnt = 0
net = ip_network('123.222.111.192/255.255.255.192', 0)
for ip in net:
    if f'{ip:b}'[24:].count('1') % 3 != 0:
        cnt += 1
print(cnt)'''#Answer: 43
"""
