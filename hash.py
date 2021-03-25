#!/usr/bin/python

import csv
import datetime
import hashlib
import os

bad = ["/usr", "/boot", "/bin", "/etc", "/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]
path = "/"

def main():
    if os.path.exists("hash_values.csv"):
        checkhashfile()
        exit()
    else:
        createhashfile()
        exit()

def createhashfile():
    hashlist = open("hash_values.csv","w")
    for root, d_names, f_names in os.walk(path):
        if root not in bad:
            for files in f_names:
                filepath = os.path.join(root,files)
                sha256 = hashlib.sha256()
                try:
                    f = open(filepath, "rb")
                except:
                    continue
                while True:
                    buffer1 = f.read(4096)
                    if not buffer1:
                        break
                    sha256.update(buffer1)
                f.close()
                hash1 = sha256.hexdigest()
                time = str(datetime.datetime.now())
                complete = files + "," + hash1 + "," + time + "\n"
                hashlist.write(complete)
    hashlist.close()

def checkhashfile():
    templist = []
    hashlist = open("hash_values.csv","r+")
    for root, d_names, f_names in os.walk(path):
        if root not in bad:
            for files in f_names:
                filepath = os.path.join(root,files)
                sha256 = hashlib.sha256()
                try:
                    f = open(filepath, "rb")
                except:
                    continue
                while True:
                    try:
                        buffer1 = f.read(4096)
                        if not buffer1:
                            break
                        sha256.update(buffer1)
                        time = str(datetime.datetime.now())
                    except:
                        break
                f.close()
                hash1 = sha256.hexdigest()
                complete = files + "," + hash1
                for line in hashlist:
                    line=line.strip()
                    try:
                        stuff = line.split(",")
                        oldRoot = stuff[0]
                        oldHash = stuff[1]
                        oldLine = oldRoot + "," + oldHash
                    except:
                        continue
                    if complete != oldLine:
                        templist += (complete + "," + time + "\n")
                        
    for item in templist:
        hashlist.write(item)
        print(item + ": has been changed")


main()
