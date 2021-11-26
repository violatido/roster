# **G2 ROSTER**
### Created by Ilana Mercer

#### **Requirements**
* Python 3
* Pip

#### Clone this repository
``` bash
git clone 'https://github.com/violatido/roster'
```
#### Create a virtual environment
``` bash
python3 -m venv env
```
#### activate the virtual environment
``` bash
source env/bin/activate
```
#### Install the requirements
```bash
pip3 install -r requirements.txt
```
#### Include the following in settings.py within the G2takehome folder
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}
```
#### Create the database
```bash
python3 manage.py migrate
```
#### Run the server
```bash
python3 manage.py runserver
```
#### Navigate to http://localhost:8000 in your browser

