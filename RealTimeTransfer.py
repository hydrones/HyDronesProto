#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
#                                            #
#   Script de transfert de fichier par FTP   #
#                                            #
##############################################
# 13/10/2016   JC. Poisson            Creation


# Librairies
# ----------
import sys
import os
import glob
from ftplib import FTP


# List files in the data folder
# -----------------------------
listFile = glob.glob('data/HD_*')
listFile.sort()


# Log file reading
# ---------------- 
listAlreadyTransfered = []
nameLogFile = 'LogTransfer/logtransfer.txt'
if os.path.isfile(nameLogFile):
    try:
        logFile = open(nameLogFile, 'r')
        for line in logFile:
            listAlreadyTransfered.append(line.strip())
        logFile.close()
    except:
        sys.exit(0)


# List files to tranfer
# ---------------------
listFile2Transfer = [f for f in listFile if f not in listAlreadyTransfered]


# Tranfer files and update de log file
# ------------------------------------
if len(listFile2Transfer) != 0:
    # Tranfer files
    ftpHyDrones = FTP('88.177.161.125','drones4hydro','TrumpForPresident')
    ftpHyDrones.cwd('disk1/HyDrones')
    for f2tranfer in listFile2Transfer:
        f = open(f2tranfer, 'rb')
        ftpHyDrones.storbinary('STOR ' + f2tranfer, f)
        f.close()

    # Update/Create the Log file
    if not os.path.isdir('LogTransfer'):
        os.mkdir('LogTransfer')
    else:
        try:
            logFile = open(nameLogFile, 'a')
            for transferedFile in listFile2Transfer:
                logFile.write(transferedFile+'\n')
            logFile.close()
        except:
            sys.exit(0)

else:
    print('\nNo file to transfer !\n')





