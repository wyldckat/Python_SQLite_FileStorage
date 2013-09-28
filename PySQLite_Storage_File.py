#!/usr/bin/env python

# Based on "Storing an image into SQLite"
# http://mornie.org/blog/2007/01/10/Storing-binary-data-in-SQLite/
# by Eriol (@mornie.org)

# Developed by Bruno Santos <wyldckat@github> September 2013
# Licensed as GPL v3.  See the file LICENSE in this directory or
# http://www.gnu.org/licenses/, for a description of the 
# GNU General Public License terms under which you can copy the files.

import sqlite3
import sys, getopt
import os
import lzo

def createDatabase(cur):

    cur.execute('''CREATE TABLE map (
        name varchar(260) NOT NULL PRIMARY KEY,
        compression INTEGER NOT NULL,
        data_file blob NOT NULL
        );''')

def showHelp():
    print 'test.py -c -d <database>'
    print 'test.py -l -d <database>'
    print 'test.py -s -d <database> -i <inputfile>'
    print 'test.py -s -z <0-9> -d <database> -i <inputfile>'
    print 'test.py -e -d <database> -i <file2extract> -o <outputfile>'


def storeInDatabase(cur, compressionLevel, filePathAndName):

    i = open(filePathAndName, 'rb')
    data = i.read()
    i.close()
    
    if compressionLevel > 0:
        ldata = lzo.compress(data, compressionLevel)
        data = ldata

    cur.execute("INSERT INTO map (name, compression, data_file) values (?, ?, ?) ",
                (filePathAndName, compressionLevel, sqlite3.Binary(data))
               )

               
def retrieveFromDatabase(cur, inputFile, outputFile):

    cur.execute("SELECT compression,data_file FROM map WHERE name = ?", (inputFile,))
    row = cur.fetchone()
    data = row[1]

    if row[0] > 0:
        ldata = lzo.decompress(data)
        data = ldata
    
    i = open(outputFile, 'wb')
    i.write(data)
    i.close()

    
def listFilesOnDatabase(cur):
    print "File list:"

    for row in cur.execute("SELECT name FROM map"):
        print "    ", row[0]


def main(argv):
    databasefile = ''
    inputfile = ''
    outputfile = ''
    create = False
    store = False
    extract = False
    listFiles = False
    compressionLevel = 0

    try:
        opts, args = getopt.getopt(argv,"hcselz:d:i:o:",["lzo=","dfile=","ifile=","ofile="])
        
    except getopt.GetoptError:
        showHelp()
        sys.exit(2)

    for opt, arg in opts:
      
        if opt == '-h':
            showHelp()
            sys.exit()
            
        elif opt == '-c':
            create = True
            
        elif opt == '-s':
            store = True
            
        elif opt == '-e':
            extract = True

        elif opt == '-l':
            listFiles = True

        elif opt in ("-z", "--lzo"):
            compressionLevel = int(arg)

        elif opt in ("-d", "--dfile"):
            databasefile = arg

        elif opt in ("-i", "--ifile"):
            inputfile = arg

        elif opt in ("-o", "--ofile"):
            outputfile = arg


    if not databasefile:
        print 'The -d option is missing.'
        showHelp()
        sys.exit(2)
            
    con = sqlite3.connect(databasefile)
    cur = con.cursor()

    if create:
        try:
            createDatabase(cur)
            print 'Database file "', databasefile, '" has been created.'
            print 'Total database file size: ', os.stat(databasefile).st_size

        except:
            print 'Error creating database'
        
    elif store:
        try:
            storeInDatabase(cur, compressionLevel, inputfile)
            con.commit()
            print 'File "', inputfile, '" has been stored.'
            print 'Total database file size: ', os.stat(databasefile).st_size

        except sqlite3.IntegrityError:
            print 'Failed to store file in database'

    elif extract:
        try:
            data = retrieveFromDatabase(cur, inputfile, outputfile)
            print 'File "', inputfile, '" has extracted to "', outputfile, '".'

        except sqlite3.IntegrityError:
            print 'Failed to extract file from database'
            
    elif listFiles:
        try:
            data = listFilesOnDatabase(cur)

        except sqlite3.IntegrityError:
            print 'Failed to list files on database'


if __name__ == '__main__':
    main(sys.argv[1:])


