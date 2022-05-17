FROM python:3.8
MAINTAINER Code-Challenge-Developer
WORKDIR /app
COPY . /app
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile
EXPOSE 5000
CMD ["pipenv", "run", "python","wsgi.py"]
