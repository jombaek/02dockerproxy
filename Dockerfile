# Федоров
FROM python:alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /app
COPY myproxy.py .

EXPOSE 8000
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "myproxy:app" ]
