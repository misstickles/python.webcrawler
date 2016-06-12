USE PYTHON2.7!!

# use 2.7
python -m venv venv

# use 2.7
pip install virtualenv

# use 2.7
E:\...>virtualenv venv

# Install lxml wheel from 
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
# venv\Scripts\pip install ""C:\Users\me\Downloads\lxml-3.4.4-cp35-none-win32.whl"

install pywin32 to c:\python27
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32-220		# wheel
https://sourceforge.net/projects/pywin32/files/pywin32/		# exe (use this with below)
C:\Python27\Scripts>easy_install "C:\Users\me\Downloads\pywin32-220.win-amd64-py2.7.exe"
C:\Python27\Scripts>python pywin32_postinstall.py -install

(easy_install pywin32-220.win32-py3.5.exe)


venv\Scripts\activate

pip install scrapy


scrapy startproject webcrawler

cd webcrawler

scrapy crawl name