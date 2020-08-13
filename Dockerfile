FROM python:3.8
RUN pip install pipenv
WORKDIR /project
ADD . /project
RUN pipenv lock --requirements > requirements.txt
RUN pipenv install
RUN chmod +x launch.sh
CMD ./launch.sh