# fluffy-octo-carnival
Learning Python ..

### git config
```
$ git config credential.helper store
$ git push https://github.com/ccrivelli/fluffy-octo-carnival.git
Username: <type your username>
Password: <type your password>
```

### virtualenv and repo setup
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

(env) $ deactivate

-- add env to .gitignore as it is not portable
$ vim  .gitignore

/env/*
~                                                                                                                                                                                                                  
~       


```





