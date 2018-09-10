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

ip=IP.split('/')[0]
mask=int(IP.split('/')[-1])
ip=ip.split('.')
MASK=('1'*int(mask))+('0'*(32-int(mask)))
mask1=int(MASK[0:8],2)
mask2=int(MASK[8:16],2)
mask3=int(MASK[16:24],2)
mask4=int(MASK[24:32],2)


print('\n'+'-'*30)
print(outIP.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
print(outMask.format(mask,mask1,mask2,mask3,mask4))


