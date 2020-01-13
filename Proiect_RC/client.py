#!/usr/bin/python2
import os
import socket
from functii import *


def receive_data():

    UDP_IP = "192.168.43.65"   #ip calculator
    UDP_PORT = 5005           #port
    #UDP_PORT=int(UDP_PORT)
    #UDP_IP=int( UDP_IP[:2] +'.'+UDP_IP[2:4]+'.'+UDP_IP[4:5]+'.'+UDP_IP[5:] )

    socky = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #IPv4 si UDP
    socky.bind((UDP_IP, UDP_PORT))  #asociez socket-ul creat adresei ip, interfata cu adresa UDP_IP

    #buf = 32768  #buffer mai mare, pachete mai putine
    buf = 16384
    #buf=8192
    os.remove('log_client.txt')
    f = open("received.png",'wb')


    #f = open("received.txt",'wb')

    data , addr = socky.recvfrom(buf)
    socky.sendto("Confirmat", addr)
    cont = ""
    info = []

    while True:
        print "PRIMIRE PACHETE..."
        salvare_client("PRIMIRE PACHETE..." + '\n')
        info = data.split("<->")
        #print info
        print info[1]
        salvare_client(info[1] + '\n')
        if info[1]=='gata':
            break
        #f.write(data)
        f.write(info[0])
        #buf=buf*2
        data, addr = socky.recvfrom(buf)
        socky.sendto("Confirmat", addr)


        #time.sleep(0.5)
#receive_data()