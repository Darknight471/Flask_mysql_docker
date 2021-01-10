FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
# RUN pip install MySQL-python
RUN pip install -r requirements.txt
CMD ["uwsgi", "app.ini"]
