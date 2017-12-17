# fluffy-octo-carnival
Playing around with Python to learn the language.  

Python Basic Tutorial - http://thepythonguru.com   

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

-- go into the project folder
$ cd venom

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

/venom/env/*

~
~

```

### clone repo ready to start (restore deps)
```
-- clone repo
$ git clone https://github.com/ccrivelli/fluffy-octo-carnival.git

-- go into the project folder
$ cd venom

-- create env
$ virtualenv -p /usr/bin/python3 env

-- activate env
$ source env/bin/activate

-- restore deps
(env) $ pip install -r requirements.txt 

>> if it does not work for kivy, install it manually (see kivy section below)
>> e.g. cannot install dev version 'Kivy==1.10.1.dev0' from pip


-- example execution
(env) $ python venom/run.py
1 XMR = $436.61


-- deactivate
(env) $ deactivate

```

## kivy experiments

See: https://kivy.org   


Installation - https://kivy.org/docs/installation/installation-linux.html  

```
# dnf install -y redhat-rpm-config
# dnf install -y make mercurial automake gcc gcc-c++ SDL_ttf-devel SDL_mixer-devel mesa-libGLES mesa-libGLES-devel gstreamer-plugins-good gstreamer gstreamer-python mtdev-devel python-devel  

-- important
# dnf install -y  python3-devel

-- inside virtualenv
(env) $ pip install --upgrade pip virtualenv setuptools
(env) $ pip install numpy

-- getting compilation error with cython 0.27 - https://github.com/SerpentAI/SerpentAI/issues/58   
(env) $ pip install Cython==0.26
(env) $ pip install pygame


-- install stable version of kivy 
(env) $ pip install kivy
..
Successfully installed kivy-1.10.0


OR

-- install the development version of kivy - see this issue: https://github.com/kivy/kivy/issues/5457   
(env) pip install git+https://github.com/kivy/kivy.git@master
..
Successfully installed Kivy-1.10.1.dev0




```

Create an application - https://kivy.org/docs/guide/basic.html#quickstart   

#### post install taks

```


-- add permissions for event
# usermod -a -G input lotek


$ ls -ltrl /dev/input/event7
crw-rw----. 1 root input 13, 71 Dec 13 16:36 /dev/input/event7

-- otherwise get this error
[WARNING] [MTD         ] Unable to open device "/dev/input/event7". Please ensure you have the appropriate permissions.


```

Understanding Widgets - https://kivy.org/docs/tutorials/firstwidget.html  
Kv language - https://kivy.org/docs/guide/lang.html  


## sublime settings (tabs into space)
```
"tab_size": 4,
"translate_tabs_to_spaces": true
```

## notes

- cpuminer (ltc) to test  
- python miners to reasearch (ltc)
- visual miner (like a game), see all the user connected to help you ...
- twisted framework (event-driven networking engine written in Python) - https://twistedmatrix.com/   
- flask microframework (for web apps) - http://flask.pocoo.org/




