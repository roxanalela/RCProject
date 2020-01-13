#!/usr/bin/python2


def salvare_date(data):
	fd = open('text.txt', 'a')
	fd.write(data)
	fd.close()

def salvare_server(data):
	fd = open('log_server.txt', 'a')
	fd.write(data)
	fd.close()

def salvare_client(data):
	fd = open('log_client.txt', 'a')
	fd.write(data)
	fd.close()


def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()