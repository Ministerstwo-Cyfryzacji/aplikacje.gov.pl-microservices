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
    docker build -t messageboard .
    docker run -p 5001:80/tcp -v /tmp/messageboard:/shared messageboard init_db.py
    docker run -p 5001:80/tcp -v /tmp/messageboard:/shared messageboard app.py --self-public-url http://172.17.0.1:5001 --dashboard-url http://172.17.0.1:5002

`-p 5001:80/tcp` denotes port redirection from `5001` on host to `80` inside container.

`-v /tmp/messageboard:/shared/` danotes that host directory `/tmp/messageboard` is mounted on continer directory `/shared`.

`172.17.0.1` is address of Docker host inside docker virtual network. It can be obtained by running `ip addr show docker0` on host. `172.17.0.1:5002` is address of dashboard service.
