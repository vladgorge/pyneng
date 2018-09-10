#!/usr/bin/env python3

#IP='10.24.1.0/24'
IP=input('Network IP : ')

outIP='''Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''

outMask='''Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:<08b} {2:<08b} {3:<08b} {4:<08b}
'''
mask=int(IP.split('/')[-1])
MASK=('1'*int(mask))+('0'*(32-int(mask)))
ip=IP.split('/')[0]
ip=ip.split('.')
ipbin='{:08b}{:08b}{:08b}{:08b}'.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))

netbin1=ipbin[:mask]
netbin2=MASK[mask:]
netbin=netbin1+netbin2

net1=int(netbin[0:8],2)
net2=int(netbin[8:16],2)
net3=int(netbin[16:24],2)
net4=int(netbin[24:32],2)

mask1=int(MASK[0:8],2)
mask2=int(MASK[8:16],2)
mask3=int(MASK[16:24],2)
mask4=int(MASK[24:32],2)

print('\n'+'-'*30)
print(outIP.format(net1,net2,net3,net4))
print(outMask.format(mask,mask1,mask2,mask3,mask4))






