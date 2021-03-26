#!/usr/bin/python
#Used online resources like:
#stackoverflow.com/questions/22058048/hashing-a-file-in-python
#bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php

import csv
import datetime
import hashlib
import os

bad = ["/usr", "/boot", "/bin", "/etc", "/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]
path = "/"
filename = "hash_values1.csv"
writeMode = "w"
readPlus = "r+" 

def main():
    if os.path.exists(filename):
        print("Checking " + filename)
        checkhashfile(filename,readPlus)
        exit()
    else:
        print("Creating " + filename)
        createhashfile(filename,writeMode)
        exit()

def createhashfile(filename, mode):
    hashlist = open(filename,mode)
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
                        buffer1 = f.read(65536)
                        if not buffer1:
                            break
                        sha256.update(buffer1)
                    except:
                        break
                f.close()
                hash1 = sha256.hexdigest()
                time = str(datetime.datetime.now())
                complete = files + "," + hash1 + "," + time + "\n"
                hashlist.write(complete)
    hashlist.close()

def checkhashfile(filename, mode):
    templist = []
    hashlist = open(filename,mode)
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
                        buffer1 = f.read(65536)
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
