FROM python:3.11.6

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]