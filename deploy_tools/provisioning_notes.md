Provisioning a new Django site
==============================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

    /home/username
    └── sites
        └── SITENAME
            ├── database
            ├── source
            ├── static
            └── virtualenv

## virtualenv

    $ cd /home/username/sites/SITENAME/source/
    $ virtualenv --python=python3 ../virtualenv
    $ source ../virtualenv/bin/activate
    $ pip install ...
    $ pip freeze > requirements.txt
    $ deactivate                                   

    $ virtualenv --python=python3 ../virtualenv/
    $ ../virtualenv/bin/pip install -r requirements.txt

## Gunicorn

    $ cd /home/username/sites/SITENAME/source/
    $ ../virtualenv/bin/pip install gunicorn
    $ ../virtualenv/bin/gunicorn service.wsgi:application
