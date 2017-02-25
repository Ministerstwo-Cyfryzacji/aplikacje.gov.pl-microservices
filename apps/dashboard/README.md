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
