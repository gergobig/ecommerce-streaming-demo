FROM python:3.11-slim

WORKDIR /srv
ENV PYTHONPATH=/srv

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
