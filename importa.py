#! /usr/bin/env python
# -*- coding: utf-8 -*-
#   Gter Copyleft 2018
#   Roberto Marzocchi

import os

import psycopg2
from conn import *

import csv
import logging
import tempfile

tmpfolder=tempfile.gettempdir() # get the current temporary directory
logfile='{}\import_volontari.log'.format(tmpfolder)
if os.path.exists(logfile):
    os.remove(logfile)

logging.basicConfig(format='%(asctime)s\t%(levelname)s\t%(message)s',
    filename=logfile,
    level=logging.INFO)


logging.info('Inizio a leggere il file CSV')

nome=[]
cognome=[]
cf=[]
id1=[]
id2=[]

#*****************************
# sostituire nome file csv
#*****************************
with open('GRUPPO_GENOVA.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i=0;
    for row in spamreader:
            if i> 0:
                #print(row)
                nome.append(row[0])
                cognome.append(row[1])
                cf.append(row[2])
                id1.append(int(row[3]))
                id2.append(int(row[4]))
                #print(nome)
            i+=1

nrows=len(cf)
logging.info('Lette {} righe'.format(nrows))



try:
    # Connect to an existing database
    con = psycopg2.connect(host=ip, port=port, dbname=db, user=user, password=pwd)
    logging.info("connected to DB emergenze!")
except psycopg2.Error as e:
    logging.error("unable to connect")
    logging.error(e.pgerror)
    exit()


# Open a cursor to perform database operations
cur = con.cursor()
con.autocommit = True

i=0
cont=0
while i < nrows:
    #*****************************
    # caso  con id1 e id2
    #*****************************
    query="""
        INSERT INTO users.utenti_esterni(cf, nome, cognome, id1, id2)
        VALUES (%s, %s, %s, %s, %s);
        """
    data=(cf[i], nome[i], cognome[i], id1[i], id2[i], )
    #*****************************
    # caso  con solo id1 
    #*****************************
    # query="""
    #     INSERT INTO users.utenti_esterni(cf, nome, cognome, id1)
    #     VALUES (%s, %s, %s, %s);
    #     """
    # data=(cf[i], nome[i], cognome[i], id1[i], )
    
    try:
        cur.execute(query,data)
        logging.info('Successfully inserted the following CF '.format(cf[i]))
        cont+=1
    except psycopg2.Error as e:
        logging.error('Error executing the following query')
        logging.error(e.pgerror)
    i+=1

logging.info('Inseriti {} nuovi record'.format(cont))