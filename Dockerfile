FROM python:3.7.2

# RUN pip install uwsgi

COPY . /srv/www

WORKDIR /srv/www

RUN pip install -r requirements.txt

# CMD ["uwsgi","--http",":5000","--manage-script-name","--mount","/=app:app"]
CMD ["gunicorn","-w","4","app:app","--bind=0.0.0.0:5000"]
