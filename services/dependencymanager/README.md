Installation
============

* install Python 3 and python-virtualenv,
* run `virtualenv -p /usr/bin/python3 venv` to create the virtual Python environment,
* run `. venv/bin/activate` to enter the virtual Python environment,
* run `pip install -r requirements.txt` to install required Python packages in the virtual
  environment,
* copy the settings from `settings.py.example` to `settings.py`, customizing it if needed,
* run the app via `python app.py`.

Run in Docker container
=======================

    cp settings.py.example_docker settings.py
    docker build -t dependencymanager .
    docker run -p 5000:80/tcp dependencymanager

`-p 5000:80/tcp` denotes port redirection from 5000 on host to 80 inside container.
