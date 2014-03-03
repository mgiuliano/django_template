django-template
===============

Resources for Django Web Development

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
