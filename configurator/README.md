Configurator
============

Configurator is a 'package manager' for a signle instance of
aplikacje.gov.pl platform. Mainly it is responsible for configuring and
deploying apps in containers, on Docker Swarm. Apart from that it handles
other tasks such as creation of database users for installed apps.
Configurator is responsible for keeping all dependencies satisfied.

How to run
----------

Configurator is written in Python 3.

In this directory run:

    virtualenv venv
    . ./venv/bin/activate
    pip install -r requiremets.txt
    ./manage.py migrate
    ./manage.py runserver
