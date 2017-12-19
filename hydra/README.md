# hydra

Python and SecurityCenter5   

https://github.com/SteveMcGrath/pySecurityCenter    

## setting up virtualenv 
```

-- go to project folder
$ cd hydra

-- create virtual env
$ virtualenv -p /usr/bin/python3 env

-- activate to work and save deps, then deactivate
$ source env/bin/activate

-- install pysecuritycenter
(env) $ pip install pysecuritycenter

-- create code folder
$ mkdir code


```

## Install Python3 isolated env (tested on RHEL7)





###Option1 - Compile in a separate folder (Working)

ref. http://rspeer.github.io/blog/2014/03/31/python-3-4-from-scratch/   

```
# yum groupinstall 'Development Tools'
# yum install openssl-devel ncurses-devel zlib-devel glibc-devel readline-devel gdbm-devel sqlite-devel bzip2-devel xz-devel tk-devel


-- Download source from https://www.python.org/downloads/  
$ cd python3-code
$ wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz

-- compile
$ tar xvf Python-3.6.3.tar.xz 
$ cd Python-3.6.3/
$ ./configure && make

ISSUE: if you get the following error, you probably are running on a partition mounted with noexec parameter
-bash: ./configure: Permission denied

-- check 
$ ./python --version
Python 3.6.3

-- create virtual env

# mkdir env
# Python-3.6.3/python -m venv env

-- activate
# source env/bin/activate
(env) python3-code# which python
/opt/python3-code/env/bin/python
(env) python3-code# python --version
Python 3.6.3

(env) python3-code$ pip --version
pip 9.0.1 from /opt/python3-code/env/lib/python3.6/site-packages (python 3.6)


ISSUE: ssl certificate error on pip
-- workaround
$ (env) pip install --trusted-host pypi.python.org pip --upgrade


-- install modules
$ (env) pip install --trusted-host pypi.python.org pysecuritycenter
$ (env) pip install --trusted-host pypi.python.org netaddr


-- save deps
$ pip freeze > requirements.txt


-- deactivate
$ deactivate



```

###Option2 - dnf download on a different machine (Fedora 26) 
```

# dnf download --resolve python3
# dnf download --resolve python3-pip
```

Deps Issue when installing system-python-libs:
```

# rpm -ivh system-python-libs-3.6.3-2.fc26.i686.rpm
warning: system-python-libs-3.6.3-2.fc26.i686.rpm: Header V3 RSA/SHA256 Signature, key ID 64dab85d: NOKEY
error: Failed dependencies:
    glibc(x86-32) >= 2.24.90-26 is needed by system-python-libs-3.6.3-2.fc26.i686
    libbz2.so.1 is needed by system-python-libs-3.6.3-2.fc26.i686
    libc.so.6(GLIBC_2.25) is needed by system-python-libs-3.6.3-2.fc26.i686
    libcrypto.so.1.1 is needed by system-python-libs-3.6.3-2.fc26.i686
    libcrypto.so.1.1(OPENSSL_1_1_0) is needed by system-python-libs-3.6.3-2.fc26.i686
    libexpat.so.1 is needed by system-python-libs-3.6.3-2.fc26.i686
    libffi.so.6 is needed by system-python-libs-3.6.3-2.fc26.i686
    libgdbm.so.4 is needed by system-python-libs-3.6.3-2.fc26.i686
    libgdbm_compat.so.4 is needed by system-python-libs-3.6.3-2.fc26.i686
    libncursesw.so.6 is needed by system-python-libs-3.6.3-2.fc26.i686
    libpanelw.so.6 is needed by system-python-libs-3.6.3-2.fc26.i686
    libreadline.so.7 is needed by system-python-libs-3.6.3-2.fc26.i686
    libsqlite3.so.0 is needed by system-python-libs-3.6.3-2.fc26.i686
    libssl.so.1.1 is needed by system-python-libs-3.6.3-2.fc26.i686
    libssl.so.1.1(OPENSSL_1_1_0) is needed by system-python-libs-3.6.3-2.fc26.i686
    libtinfo.so.6 is needed by system-python-libs-3.6.3-2.fc26.i686

``

## Python - IP Addresses, Subnets and Ranges

http://netaddr.readthedocs.io/en/latest/tutorial_01.html   

