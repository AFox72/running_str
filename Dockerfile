FROM python:3.9.19-alpine3.20

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]