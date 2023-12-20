#!/usr/bin/python3
FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y dos2unix
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
RUN apt-get install python3-tk -y
RUN apt-get install memcached -y
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/kck
COPY requirements.txt start-server.sh /opt/app/

# Windows script dos2unix
COPY start-server.sh /opt/app/start-server.sh
RUN dos2unix /opt/app/start-server.sh && chmod +x /opt/app/start-server.sh
RUN pip install gunicorn

# COPY .pip_cache /opt/app/pip_cache/
COPY . /opt/app/kck/
RUN pip install -r /opt/app/requirements.txt --cache-dir /opt/app/pip_cache
RUN chmod -R 755 /opt/app/kck/

RUN chown -R www-data:www-data /opt/app/kck/

WORKDIR /opt/app/kck

VOLUME /var/log/nginx

RUN service memcached start 

EXPOSE 8000
STOPSIGNAL SIGTERM
ENTRYPOINT ["/opt/app/start-server.sh"]

# WORKDIR /code
# COPY requirements.txt /code/

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . /code/
