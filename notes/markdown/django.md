
# Virtual environment


```python
virtualenv --python=python3.4 myvenv

source myvenv/bin/activate

pip install django

deactivate

```

# ORM Django shell


```python

python manage.py shell

album1.song_set.create(.........)
```

# Tests


```python
Download geckodriver for firefox

tar -xvf ***.tar
chmod u + x geckodriver
mv geckodriver /usr/local/bin

or 

add file location in PATH ( gedit ~/.bashrc)


coverage run --source='.' manage.py test
coverage report
coverage html

```

# manage.py


```python
python manage.py makemigrations ****

python manage.py migrate

python manage.py sqlmigrate **music *001


python manage.py createsuperuser

## warning when running commands in containers
## because no i/o interaction
python manage.py collectstatic --no-input
```

# Translations


```python
python manage.py makemessages -l fr
python manage.py compilemessages -l fr
```
