FROM python:3.10

WORKDIR /node

RUN pip install --upgrade pip

COPY requirements.txt /node

RUN pip install -r requirements.txt

COPY . .