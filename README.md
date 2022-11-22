# Secret Santa Generator 

## Overview
Secret Santa project is created with intention to mimic a group game of the same name. There are several versions of the game but this project
is designed to follow the basic concept of it. The project is intended to be used as fun activity for an office team and number of participants is not limited. 
Refer to *Secret Santa - documentation.docx* file for more details.

## Objectives
Web application randomly matches registered users into pairs and lists them for gift giving process. If there is an uneven number of participants,
the person without pair is listed separately. Upon login, regular participants (Employees) are informed of who their match is while Administrators 
can see and reset Santa’s list and view, create and delete users from both groups. 

Matching pairs algorithm works on following rules:
-	No person can be assigned to itself (there’s no x-x pair)
-	Once matched, the pair won’t appear more than once on the list. 
-	Person can be sorted into only one role per pair. (if x is matched to y as a giver, x has to be matched to z as a receiver but cannot be matched 
  to y as receiver nor it can be matched to z as a giver)

## Quick start
To get this project running, install python and isolate the project in virtual environment: 
```python
pip install virtualenv 
virtualenv <your_env_name>
```
Activate virtual environment and install requirements
```
cd <your_env_name_folder_path>
source your_env_name/bin/activate
pip install -r requirements.txt
```

Setup Django project
```
python manage.py migrate
pyton manage.py runserver
```
App will run on default port 8000. In case the port is taken, run `python manage.py runserver 127.0.0.1:<desired_port>`

IMPORTANT
SECRET_KEY is purpusaly left empty in settings.py. Please insert your own or generate dummy one at: https://djecrety.ir/ 
This project requires groups from Django's authorisation system. Follow the steps below to create superuser, enter Django admin board and create groups. 

- `python manage.py createsuperuser` (command will prompt you to enter username, email and password which will be used for accesing Django administration board)
- `python manage.py runserver`
- Open your localhost equivalent of http://127.0.0.1:8000/admin/ in browser and login
- Add groups *Administrators* and *Employees* (names are case sensitive).
- Navigate to your localhost equivalent of http://127.0.0.1:8000/ and enjoy

Upon finish, don't forget to deactivate virtual environment: 'deactivate` 

