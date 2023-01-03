FROM python:3.9.6-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "config.wsgi:application"]