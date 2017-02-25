FROM python:3-onbuild

RUN ["mv", "settings.py.example_docker", "settings.py"]

ENTRYPOINT ["python", "app.py"]
