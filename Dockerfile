FROM python:3.10

WORKDIR /flask-api

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--env-file=.env", "run"]