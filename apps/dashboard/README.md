Installation
============

* install Python 3 and python-virtualenv,
* run `virtualenv -p /usr/bin/python3 venv` to create the virtual Python environment,
* run `. venv/bin/activate` to enter the virtual Python environment,
* run `pip install -r requirements.txt` to install required Python packages in the virtual
  environment,
* copy the settings from `settings.py.example` to `settings.py`, customizing it if needed,
* create the database via `python init_db.py`,
* run the app via `python app.py`.

Run in Docker container
=======================

    cp settings.py.example_docker settings.py
    docker build -t dashboard .
    docker run -p 5002:80/tcp -v /tmp/dashboard:/shared dashboard init_db.py
    docker run -p 5002:80/tcp -v /tmp/dashboard:/shared dashboard

`-p 5002:80/tcp` denotes port redirection from 5002 on host to 80 inside container.

`-v /tmp/dashboard:/shared/` danotes that host directory `/tmp/dashboard` is mounted on continer directory `/shared`.
