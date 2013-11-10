Python_SQLite_FileStorage
=========================

Simple Python script for storing/extracting files inside a single SQLite database file.

Based on "Storing an image into SQLite": http://mornie.org/blog/2007/01/10/Storing-binary-data-in-SQLite/ - by Eriol (@mornie.org)

GZip version based on "HTTP Compression in python and jython": http://jython.xhaus.com/http-compression-in-python-and-jython/#gzip

Developed by Bruno Santos <wyldckat@github> September 2013

Licensed as GPL v3.  See the file LICENSE in this directory or http://www.gnu.org/licenses/, for a description of the GNU General Public License terms under which you can copy the files.


How to install
==============

  * You need LZO and Python with SQLite for `PySQLite_Storage_File.py`
  * You need Python with SQLite and BZip2 for `PySQLite_Storage_File_BZ2.py`
  * You need Python with SQLite and GZip for `PySQLite_Storage_File_gzip.py`


Build and Install LZO
---------------------

LZO for Python is non-standard, but you can follow these instructions for building and installing in your home folder (at least on Linux):

```
mkdir preparing
cd preparing

wget http://www.oberhumer.com/opensource/lzo/download/lzo-2.06.tar.gz
tar -xf lzo-2.06.tar.gz
cd lzo-2.06

./configure --prefix=$HOME/lzo
make CFLAGS=-fPIC
make install

cd ..

wget https://github.com/jd-boyd/python-lzo/archive/master.zip -O python-lzo.zip
unzip python-lzo.zip
cd python-lzo-master
sed -i -e 's="/usr/include/lzo"="'$HOME/lzo/include/lzo'"=' setup.py
sed -i -e 's=##library_dirs=library_dirs=' setup.py
sed -i -e 's="/usr/local/lib"="'$HOME/lzo/lib'"=' setup.py

make
cp build/lib.*/*.so $HOME/lzo/lib/

cd ../..

echo "You can now delete this folder: $PWD/preparing"
echo "The resulting LZO files are located at $HOME/lzo"
```


Installing the Python scripts
-----------------------------

As for the scripts `PySQLite_Storage_File*.py`, since this is only a proof of concept, you can either:

  * Clone the repository https://github.com/wyldckat/Python_SQLite_FileStorage.git
  * Or download and unzip the file https://github.com/wyldckat/Python_SQLite_FileStorage/archive/master.zip

If you want the scripts to be executable on Linux, run:

```
chmod +x PySQLite_Storage_File*.py
```


How to use `PySQLite_Storage_File*.py`
=====================================

First of all, the LZO libraries need to be in Python's search path. To do this, run:

```export PYTHONPATH=$HOME/lzo/lib:$PYTHONPATH```

Then to run the script, here are the several options:

  * To create the database file: `script.py -c -d <databaseFile>`
  * To list files inside the database file: `script.py -l -d <databaseFile>`
  * To store a file without compression: `script.py -s -d <database> -i <inputfile>`
  * To store a folder without compression: `script.py -s -d <database> -f <inputfolder>`
  * To store file with compression: `script.py -s -z <0-9> -d <database> -i <inputfile>`
  * To store folder with compression: `script.py -s -z <0-9> -d <database> -f <inputfolder>`
  * To get the file back: `script.py -e -d <database> -i <file2extract> -o <outputfile>`

Where `script.py` can be any of the following:

  * You need LZO and Python with SQLite for `PySQLite_Storage_File.py`
  * You need Python with SQLite and BZip2 for `PySQLite_Storage_File_BZ2.py`
