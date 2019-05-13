FROM python:3.7

WORKDIR /app
COPY . .
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 80
ENTRYPOINT [ "python", "run.py" ]
