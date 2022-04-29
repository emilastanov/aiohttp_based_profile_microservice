FROM python:3.7

WORKDIR /application

COPY requirements.txt /application

RUN pip install -r requirements.txt

COPY . /application

CMD ["python", "main.py"]