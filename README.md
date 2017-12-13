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

-- example execution
(env) $ python venom/run.py
1 XMR = $436.61

-- restore deps
(env) $ pip install -r requirements.txt 

-- deactivate
(env) $ deactivate

```




