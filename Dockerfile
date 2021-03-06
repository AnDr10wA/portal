FROM python:latest
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
RUN apt-get update \
    && apt-get install -y postgresql-client

COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY . /code/
WORKDIR code/portal
CMD python3 manage.py makemigrations
CMD python3 manage.py migrate
CMD gunicorn portal.wsgi:application --bind 0.0.0.0:8000


