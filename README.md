# fluffy-octo-carnival
Learning Python ..

### git config
```
$ git config credential.helper store
$ git push https://github.com/ccrivelli/fluffy-octo-carnival.git
Username: <type your username>
Password: <type your password>
```

### useful git commands
```
-- work on develop branch
$ git add -A
$ git commit -m 'commit name'
$ git push origin develop

-- show branch
$ git branch

-- work on master branch
$ git checkout master
$ git merge develop master
$ git push origin master

```

### virtual environment and .gitignore (save deps)

The virtualenv needs to be created on the local machine as it's not portable.
Only the project folder goes to github repository.


```
-- install
$ pip install virtualenv --user

-- create venv
$ virtualenv -p /usr/bin/python3 env

-- activate to work and save deps, then deactivate
$ source env/bin/activate

(env) $ pip install requests
(env) $ pip install bs4
(env) $ pip freeze >  requirements.txt

-- example execution
(env) $ python venom/run.py 
1 XMR = $436.61

(env) $ deactivate

-- add env to .gitignore as it is not portable
$ vim  .gitignore

/env/*
~
~

```

### clone repo ready to start (restore deps)
```
-- clone repo
$ git clone https://github.com/ccrivelli/fluffy-octo-carnival.git

-- create env
$ virtualenv -p /usr/bin/python3 env

-- activate env
$ source env/bin/activate

-- restore deps
(env) $ pip install -r requirements.txt 

-- example execution
(env) $ python venom/run.py
1 XMR = $436.61


-- deactivate
(env) $ deactivate

```

## kivy experiments

See: https://kivy.org   
RPM for Fedora 26: https://fedora.pkgs.org/26/rpm-sphere/python-kivy-1.9.1-3.1.x86_64.rpm.html  

```
# cd /etc/yum.repos.d/
# vim rpm-sphere.repo

[rpm-sphere]
name=RPM Sphere
baseurl=http://ftp.gwdg.de/pub/opensuse/repositories/home:/zhonghuaren/Fedora_26/
gpgkey=http://ftp.gwdg.de/pub/opensuse/repositories/home:/zhonghuaren/Fedora_26/repodata/repomd.xml.key
enabled=1
gpgcheck=1


# dnf install python-kivy

(TODO)



```

