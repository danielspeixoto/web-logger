FROM python:3.8
RUN pip install pipenv
WORKDIR /project
ADD Pipfile /project
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
ADD . /project
CMD NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python3 wsgi.py