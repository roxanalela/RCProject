#!/usr/bin/python2
import os
import socket
import random as rand
from time import sleep


from functii import *
socky = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def send_data():

    UDP_IP = "192.168.43.65"
    UDP_PORT = 5005
    #UDP_IP = int(UDP_IP[:2] + '.' + UDP_IP[2:4] + '.' + UDP_IP[4:5] + '.' + UDP_IP[5:])
    #UDP_PORT=int(UDP_PORT)

    print  "UDP target IP:", UDP_IP
    salvare_server("UDP target IP:" + str(UDP_IP) +'\n')
    print  "UDP target port:", UDP_PORT
    salvare_server("UDP target port:" + str(UDP_PORT)+'\n')

    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    os.remove('log_server.txt')
    f=open("imagine.png", "rb")
    #f=open ("mama.txt", "rb")
    #print type(f)
    #print sys.getsizeof(f)
    buf = 512  #alegem dimensiunea buffer ului, in functie de el, setam valorile parametrilor

    count = 1
    etapa = 0
    confirmari_duplicate = 1

    prag=4096 #512*8
    fereastra_congestie=512 # 1SMS
    timeout=6144 #512*12

    data = True
    while (data):
        data = f.read(fereastra_congestie)
        if not data:
            break
        if etapa==0:
            print "Fereastra ",fereastra_congestie###
            print "Confirmari duplic",confirmari_duplicate
            print "SLOW START ",fereastra_congestie/512
            salvare_server("SLOW START " + str(fereastra_congestie/512)+'\n')
            if fereastra_congestie<prag:
                print "Confirmari duplic", confirmari_duplicate
                print "Fereastra ",fereastra_congestie ###
                print "prag",prag ##
                print "VALELEU 1 \n"
                socky.sendto(data + "<->" + str(count), (UDP_IP, UDP_PORT))
                #print(data + "<->" + str(count), (UDP_IP, UDP_PORT))
                # primesc ACK
                recv_data, addr = socky.recvfrom(2048)

                print  "ACKNOWLEDGEMENT: ",recv_data
                salvare_server("ACKNOWLEDGEMENT: " + str(recv_data)+'\n')
                salvare_date(str(count)+','+str(fereastra_congestie / 512)+'\n')
                count += 1
                fereastra_congestie*=2
            elif fereastra_congestie>=prag:
                print "Confirmari duplic", confirmari_duplicate
                print "Fereastra ", fereastra_congestie  ###
                print "prag", prag  ##
                print "VALELEU 2 \n"
                socky.sendto(data + "<->" + str(count), (UDP_IP, UDP_PORT))
                # primesc ack
                recv_data, addr = socky.recvfrom(2048)

                print  "ACKNOWLEDGEMENT: ", recv_data
                salvare_server("ACKNOWLEDGEMENT: " + str(recv_data)+'\n')
                salvare_date(str(count) + ',' + str(fereastra_congestie / 512) + '\n')
                fereastra_congestie += 512
                count += 1
                etapa=1
                continue
            else:
                print 'error'
        elif etapa==1:
            print "Fereastra ", fereastra_congestie  ###
            print "Confirmari duplic", confirmari_duplicate
            print "prag", prag  ##
            print "CONGESTION AVOIDANCE", fereastra_congestie/512
            salvare_server("CONGESTION AVOIDANCE"+str(fereastra_congestie/512)+'\n')
            if fereastra_congestie<timeout:
                print "Confirmari duplic", confirmari_duplicate
                print "Fereastra ", fereastra_congestie  ###
                print "prag", prag  ##
                print "VALELEU 3 \n"
                socky.sendto(data + "<->" + str(count), (UDP_IP, UDP_PORT))
                # primesc ack
                recv_data, addr = socky.recvfrom(2048)

                print "ACKNOWLEDGEMENT: ", recv_data
                salvare_server("ACKNOWLEDGEMENT: " + str(recv_data)+'\n')
                salvare_date(str(count) + ',' + str(fereastra_congestie / 512) + '\n')
                fereastra_congestie += 512
                count += 1
            elif fereastra_congestie>=timeout:
                print "Confirmari duplic", confirmari_duplicate
                print "Fereastra ", fereastra_congestie  ###
                print "prag", prag  ##
                print "VALELEU 4 \n"
                socky.sendto(data + "<->" + str(count), (UDP_IP, UDP_PORT))
                # primesc ack
                recv_data, addr = socky.recvfrom(2048)

                print "ACKNOWLEDGEMENT: ", recv_data
                salvare_server("ACKNOWLEDGEMENT: " + str(recv_data)+'\n')
                salvare_date(str(count) + ',' + str(fereastra_congestie / 512) + '\n')
                prag=fereastra_congestie/2
                fereastra_congestie=prag
                count += 1
                etapa=2
                continue
            else:
                print "Error case 1"

        elif etapa==2 and confirmari_duplicate<=2:
            print "Confirmari duplic", confirmari_duplicate
            print "Fereastra ", fereastra_congestie  ###
            print "prag", prag  ##
            print "FAST RECOVERY", fereastra_congestie / 512
            salvare_server("FAST RECOVERY" + str(fereastra_congestie / 512)+'\n')
            if fereastra_congestie < timeout:
                print "Confirmari duplic", confirmari_duplicate
                print "Fereastra ", fereastra_congestie  ###
                print "prag", prag  ##
                print "VALELEU 5 \n"
                socky.sendto(data + "<->" + str(count), (UDP_IP, UDP_PORT))
                # primesc ack
                recv_data, addr = socky.recvfrom(2048)

                print "ACKNOWLEDGEMENT: ", recv_data
                salvare_server("ACKNOWLEDGEMENT: " +str(recv_data)+'\n')
                salvare_date(str(count) + ',' + str(fereastra_congestie / 512) + '\n')
                fereastra_congestie += 512
                count += 1
            elif fereastra_congestie >= timeout and confirmari_duplicate<2:
                print "Confirmari duplic", confirmari_duplicate
                print "Fereastra ", fereastra_congestie  ###
                print "prag", prag  ##
                print 'VALELEU 6 \n'
                socky.sendto(data + "<->" + str(count), (UDP_IP, UDP_PORT))
                # primesc ack
                recv_data, addr = socky.recvfrom(2048)

                print "ACKNOWLEDGEMENT: ", recv_data
                salvare_server("ACKNOWLEDGEMENT: " + str(recv_data)+'\n')
                salvare_date(str(count) + ',' + str(fereastra_congestie / 512) + '\n')
                prag = fereastra_congestie / 2
                fereastra_congestie = prag
                etapa = 2
                confirmari_duplicate+=1
                count += 1



                continue
            elif fereastra_congestie >= timeout and confirmari_duplicate == 2:
                print "Confirmari duplic", confirmari_duplicate
                print "Fereastra ", fereastra_congestie  ###
                print "prag", prag  ##
                print 'VSLELEU 7 \n'
                socky.sendto(data + "<->" + str(count), (UDP_IP, UDP_PORT))
                # primesc ack
                recv_data, addr = socky.recvfrom(2048)

                print "ACKNOWLEDGEMENT: ", recv_data
                salvare_server("ACKNOWLEDGEMENT: " + str(recv_data)+'\n')
                salvare_date(str(count) + ',' + str(fereastra_congestie / 512) + '\n')
                prag = 4096
                fereastra_congestie = 512
                etapa = 0
                count += 1
                confirmari_duplicate = 1


                print "TIMEOUT ", timeout
                print "THRESHOLD ", prag
                salvare_server("TIMEOUT " + str(timeout)+'\n')
                salvare_server("THRESHOLD " + str(prag)+'\n')
                continue
            else:
                print "Error case 2"

        sleep(1)

    socky.sendto(" " + "<->" + 'gata', (UDP_IP, UDP_PORT))
    socky.close()

    print "NUMAR PACHETE ", count
    salvare_server("NUMAR PACHETE " + str(count)+'\n')
#send_data()