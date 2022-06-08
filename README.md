## HR System Backend

## Technology Stack

- [Python 3.8][1]
- [Pip][2]
- [Virtualenv][3]
- [Docker][4]

## Installation Guide

### 1. Install [Python 3.8][1]
    # https://www.python.org/downloads/

### 2. Install [Pip][2]
    $ sudo apt install python3-pip

### 3. Install [Virtualenv][3]
    $ pip install virtualenv

### 4. Clone the repository
	$ git clone https://github.com/azez-alhoot/hr_backend.git
	$ cd hr_backend

### 5. Create new virtualenv and use it
    $ virtualenv venv
    $  source venv/bin/activate
    
### 6. Install dependencies
On the project root there is a requirements.txt file.  
Make sure you install all the required dependencies before running app.  

    $ pip install -r requirements.txt
 
### 7. Setup environment variables
    $ mv .env.sample .env
    # open .env file and enter values for environment variables

### 8. Run App
    $ python mange.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver

## Installation Guide (Using Docker)

### 1. Install [Docker][4]
   The following is the single command required to install Docker on macOS using Homebrew.
   
    $ brew cask install docker

### 2. Clone the repository
	$ git clone https://github.com/azez-alhoot/hr_backend.git
	$ cd order-integration

### 3. Setup environment variables
    $ mv deploy/development/config/app/.env.sample deploy/development/config/app/.env
    # open deploy/development/config/app/.env file and enter values for environment variables

### 4. Run App
    $ docker-compose -f deploy/development/docker-compose.yml up --build

## Notes
    This APIs for HR system that enable candidates to apply for jobs and HR managers to check their requests  
    

## Copyright
Copyright (c) 2022 Abedalaziz Alissa.


[1]: https://www.python.org/downloads/
[2]: https://pypi.org/project/pip/
[3]: https://virtualenv.pypa.io/en/latest/
[4]: https://www.docker.com/