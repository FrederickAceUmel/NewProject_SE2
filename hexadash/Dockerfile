FROM python:3.12.4
RUN useradd -ms /bin/sh -u 1001 app
USER app

WORKDIR /app

EXPOSE 8000

COPY requirements.txt ./
RUN pip3 install -r requirements.txt --no-cache-dir

COPY --chown=app:app . /app
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]