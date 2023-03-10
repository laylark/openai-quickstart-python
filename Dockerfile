FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.lock requirements.lock
RUN pip3 install -r requirements.lock

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]