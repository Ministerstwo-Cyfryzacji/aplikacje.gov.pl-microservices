FROM python:3-onbuild

RUN ["mv", "settings.py.example_docker", "settings.py"]

RUN ["mkdir", "/shared"]
VOLUME ["/shared"]

ENTRYPOINT ["python", "app.py"]
