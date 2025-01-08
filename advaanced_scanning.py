#!/usr/bin/python

#

from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print(f'tgtPort is open')
    except:
        print(f'tgtPort is closed')
    finally:
        sock.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('unknown host')
    try:
        tgtName = gethostbyaddress(tgtIP)
        print('scan results for: ',tgtName[0])
    except:
        print('scan results for: ',tgtIP)
    setdefaulttimeout(2)
    for tgtPort in tgtPorts:
        t= Thread(target= connScan,args=(tgtHost,tgtPort))
        t.start()
    
def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -P <target port>')
    parser.add_option('-H',dest='tgtHost', type= 'string', help='specify target host')
    parser.add_option('-P',dest='tgtPort', type= 'string', help='specify target port seperated by comma ')
    (options, args)=parser.parse_args()
    tgtHost=options.tgtHost
    tgtPorts = list(map(int, str(options.tgtPort).split(',')))
    # tgtPorts=str(options.tgtPort).split(',')
    if (tgtHost==None) | (tgtPorts[0]==None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)
if __name__=='__main__':
    main()
