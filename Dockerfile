FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt

EXPOSE 8000

CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]
