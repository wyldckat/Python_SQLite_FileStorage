Python_SQLite_FileStorage
=========================

Simple Python script for storing/extracting files inside a single SQLite database file.

Based on "Storing an image into SQLite": http://mornie.org/blog/2007/01/10/Storing-binary-data-in-SQLite/ - by Eriol (@mornie.org)

Developed by Bruno Santos <wyldckat@github> September 2013

Licensed as GPL v3.  See the file LICENSE in this directory or http://www.gnu.org/licenses/, for a description of the GNU General Public License terms under which you can copy the files.


How to install
==============

You need LZO and Python with SQLite. LZO is only the non-standard one, for which the following instructions should work (at least on Linux):

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

As for the script `PySQLite_Storage_File.py`, since this is only a proof of concept, you can either:

  * Clone the repository https://github.com/wyldckat/Python_SQLite_FileStorage.git
  * Or download and unzip the file https://github.com/wyldckat/Python_SQLite_FileStorage/archive/master.zip

If you want the script to be executable on Linux, run:

```
chmod +x PySQLite_Storage_File.py
```


How to use `PySQLite_Storage_File.py`
=====================================

First of all, the LZO libraries need to be in Python's search path. To do this, run:

```export PYTHONPATH=$HOME/lzo/lib:$PYTHONPATH```

Then to run the script, here are the several options:

  * To create the database file: `test.py -c -d <databaseFile>`
  * To list files inside the database file: `test.py -l -d <databaseFile>`
  * To store a file without compression: `test.py -s -d <database> -i <inputfile>`
  * To store a folder without compression: `test.py -s -d <database> -f <inputfolder>`
  * To store file with compression: `test.py -s -z <0-9> -d <database> -i <inputfile>`
  * To store folder with compression: `test.py -s -z <0-9> -d <database> -f <inputfolder>`
  * To get the file back: `test.py -e -d <database> -i <file2extract> -o <outputfile>`
