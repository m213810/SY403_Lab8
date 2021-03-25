My program creates a comma separate value (CSV) file that stores the file path, hash value of a file, and the time the value was saved. It creates the hash using SHA256. If you run the program again, it will check to see if a .csv file already exists. If it does, it will go to the checkhashfile() function which will rehash all the files in your system and check them against the old .csv file and compare them line by line to see if anything has changed. If any files have been altered since the previous test, the hashes will not match and the .csv file will be updated with the new information. After that, the program will print to the screen and alert the user to all the files that have been altered.
