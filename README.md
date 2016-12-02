# NYCCC
## What is NYCCC
**NYCCC** stand for the **N**ew **Y**ork **C**ity **C**ar **C**ollision, it's the simple web service that summarize the *Contributing Factors* of car collisions
in the *New York City* into an easy to understand and intepret pie chart.

## The open data
We use the data from the New York City's [**NYC Open Data**](https://data.cityofnewyork.us/) API. Which is being fetched live every time the webpage is loaded.

## How to use
### Live site
Just visit [http://nyccc.herokuapp.com](http://nyccc.herokuapp.com) to see the site live.

### Run on your local machine
#### Requirements
1. Python 2.7 or 3.5+, don't forget to add the *Python executable* to your *PATH* afterwards.
2. Virtualenv, can be installed after installing Python by using `pip install virtualenv`

#### Steps
Start from the command-line interface of your operating system *(e.g. Terminal, bash, Command Prompt, Powershell)*

1. Clone the repository `git clone https://github.com/benwrk/NYCCC.git`, if you don't have **Git** installed, just download the project as a ZIP file right [here](https://github.com/benwrk/NYCCC/archive/master.zip).
2. Create a virtual environment `virtualenv env`.
3. Activate the virtual environment, use `source env/bin/activate` for UNIX-based systems (including Mac and Linux). For Windows use `.\env\Scripts\activate.bat` if you are using **Windows Command Prompt**, or use `.\env\Scripts\activate` if you are using **Windows PowerShell**.
4. Install project requirements `pip install -r requirements.txt`.
5. Initialize project database `python manage.py makemigrations` and then `python manage.py migrate` right after.
6. Now we're ready, run the project. On **Windows**: `python manage.py runserver 0.0.0.0:8000`. On **UNIX-based systems**: `gunicorn NYCCC.wsgi`.
7. The site is live, visit [http://localhost:8000](http://localhost:8000) on your browser.
